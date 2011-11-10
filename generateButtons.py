#!/usr/bin/env python
"""
This script generates icons to be used within OpenLayers-applications. Requires python and inkscape.

Version:0.1
Date: 2009-07-24
Author: Marc Jansen
License: BSD License (see ./license.txt)
"""
__author__ = 'Marc Jansen'
__version__= '0.1'
__date__= '2009-07-27'
__license__= 'BSD License (see ./license.txt)'

import os
import re
import sys
# the named colors for SVGs as stated by the W3C
# http://www.w3.org/TR/css3-color/#svg-color
colorNamesAndCodes = {
    'aliceblue' : '#f0f8ff',
    'antiquewhite' : '#faebd7',
    'aqua' : '#00ffff',
    'aquamarine' : '#7fffd4',
    'azure' : '#f0ffff',
    'beige' : '#f5f5dc',
    'bisque' : '#ffe4c4',
    'black' : '#000000',
    'blanchedalmond' : '#ffebcd',
    'blue' : '#0000ff',
    'blueviolet' : '#8a2be2',
    'brown' : '#a52a2a',
    'burlywood' : '#deb887',
    'cadetblue' : '#5f9ea0',
    'chartreuse' : '#7fff00',
    'chocolate' : '#d2691e',
    'coral' : '#ff7f50',
    'cornflowerblue' : '#6495ed',
    'cornsilk' : '#fff8dc',
    'crimson' : '#dc143c',
    'cyan' : '#00ffff',
    'darkblue' : '#00008b',
    'darkcyan' : '#008b8b',
    'darkgoldenrod' : '#b8860b',
    'darkgray' : '#a9a9a9',
    'darkgreen' : '#006400',
    'darkgrey' : '#a9a9a9',
    'darkkhaki' : '#bdb76b',
    'darkmagenta' : '#8b008b',
    'darkolivegreen' : '#556b2f',
    'darkorange' : '#ff8c00',
    'darkorchid' : '#9932cc',
    'darkred' : '#8b0000',
    'darksalmon' : '#e9967a',
    'darkseagreen' : '#8fbc8f',
    'darkslateblue' : '#483d8b',
    'darkslategray' : '#2f4f4f',
    'darkslategrey' : '#2f4f4f',
    'darkturquoise' : '#00ced1',
    'darkviolet' : '#9400d3',
    'deeppink' : '#ff1493',
    'deepskyblue' : '#00bfff',
    'dimgray' : '#696969',
    'dimgrey' : '#696969',
    'dodgerblue' : '#1e90ff',
    'firebrick' : '#b22222',
    'floralwhite' : '#fffaf0',
    'forestgreen' : '#228b22',
    'fuchsia' : '#ff00ff',
    'gainsboro' : '#dcdcdc',
    'ghostwhite' : '#f8f8ff',
    'gold' : '#ffd700',
    'goldenrod' : '#daa520',
    'gray' : '#808080',
    'green' : '#008000',
    'greenyellow' : '#adff2f',
    'grey' : '#808080',
    'honeydew' : '#f0fff0',
    'hotpink' : '#ff69b4',
    'indianred' : '#cd5c5c',
    'indigo' : '#4b0082',
    'ivory' : '#fffff0',
    'khaki' : '#f0e68c',
    'lavender' : '#e6e6fa',
    'lavenderblush' : '#fff0f5',
    'lawngreen' : '#7cfc00',
    'lemonchiffon' : '#fffacd',
    'lightblue' : '#add8e6',
    'lightcoral' : '#f08080',
    'lightcyan' : '#e0ffff',
    'lightgoldenrodyellow' : '#fafad2',
    'lightgray' : '#d3d3d3',
    'lightgreen' : '#90ee90',
    'lightgrey' : '#d3d3d3',
    'lightpink' : '#ffb6c1',
    'lightsalmon' : '#ffa07a',
    'lightseagreen' : '#20b2aa',
    'lightskyblue' : '#87cefa',
    'lightslategray' : '#778899',
    'lightslategrey' : '#778899',
    'lightsteelblue' : '#b0c4de',
    'lightyellow' : '#ffffe0',
    'lime' : '#00ff00',
    'limegreen' : '#32cd32',
    'linen' : '#faf0e6',
    'magenta' : '#ff00ff',
    'maroon' : '#800000',
    'mediumaquamarine' : '#66cdaa',
    'mediumblue' : '#0000cd',
    'mediumorchid' : '#ba55d3',
    'mediumpurple' : '#9370db',
    'mediumseagreen' : '#3cb371',
    'mediumslateblue' : '#7b68ee',
    'mediumspringgreen' : '#00fa9a',
    'mediumturquoise' : '#48d1cc',
    'mediumvioletred' : '#c71585',
    'midnightblue' : '#191970',
    'mintcream' : '#f5fffa',
    'mistyrose' : '#ffe4e1',
    'moccasin' : '#ffe4b5',
    'navajowhite' : '#ffdead',
    'navy' : '#000080',
    'oldlace' : '#fdf5e6',
    'olive' : '#808000',
    'olivedrab' : '#6b8e23',
    'orange' : '#ffa500',
    'orangered' : '#ff4500',
    'orchid' : '#da70d6',
    'palegoldenrod' : '#eee8aa',
    'palegreen' : '#98fb98',
    'paleturquoise' : '#afeeee',
    'palevioletred' : '#db7093',
    'papayawhip' : '#ffefd5',
    'peachpuff' : '#ffdab9',
    'peru' : '#cd853f',
    'pink' : '#ffc0cb',
    'plum' : '#dda0dd',
    'powderblue' : '#b0e0e6',
    'purple' : '#800080',
    'red' : '#ff0000',
    'rosybrown' : '#bc8f8f',
    'royalblue' : '#4169e1',
    'saddlebrown' : '#8b4513',
    'salmon' : '#fa8072',
    'sandybrown' : '#f4a460',
    'seagreen' : '#2e8b57',
    'seashell' : '#fff5ee',
    'sienna' : '#a0522d',
    'silver' : '#c0c0c0',
    'skyblue' : '#87ceeb',
    'slateblue' : '#6a5acd',
    'slategray' : '#708090',
    'slategrey' : '#708090',
    'snow' : '#fffafa',
    'springgreen' : '#00ff7f',
    'steelblue' : '#4682b4',
    'tan' : '#d2b48c',
    'teal' : '#008080',
    'thistle' : '#d8bfd8',
    'tomato' : '#ff6347',
    'turquoise' : '#40e0d0',
    'violet' : '#ee82ee',
    'wheat' : '#f5deb3',
    'white' : '#ffffff',
    'whitesmoke' : '#f5f5f5',
    'yellow' : '#ffff00',
    'yellowgreen' : '#9acd32'
}

def cleanup_passed_color_value(s):
    """Cleans passed string to either return a valid SVG-RGB-HEX-notation or an empty string."""
    reo = re.compile('[0-9a-f]')
    cannotBeCleaned = ''
    if s[0] == '#' and len(s) in [4,7] and reo.match(s[1:]):
        return s
    if s in colorNamesAndCodes:
        col = colorNamesAndCodes[s]
        if reo.match(col[1:]):
            return col
        else:
            return cannotBeCleaned
    if len(s) in [3,6]  and reo.match(s):
        return '#' + s
    if len(s) == 2  and reo.match(s):
        return '#' +s +s +s
    return cannotBeCleaned
    
def print_usage_info_screen():
    """Prints usage information for this script."""
    print ""
    print "Usage: "
    print "  ./generateButtons.py 'background-color' 'foreground-color'"
    print ""
    print "Examples: "
    print "  ./generateButtons.py '#123456' '#ededed'"
    print "  ./generateButtons.py 'red' 'white'"
    print "  ./generateButtons.py '#123' 'purple'"
    print "  ./generateButtons.py '00e' 'fff'"
    print "  ./generateButtons.py 'ed' 'ff'"
    print ""

def print_illegal_color_format_screen( enteredBGColor, enteredFGColor, convertedBGColor, convertedFGColor ):
    """Prints debugging information when the script encounters an illegal color."""
    print ""
    print "Error: are the passed in colors valid?"
    print "  - passed in background-color '" + enteredBGColor + "' was converted to '" + convertedBGColor + "'."
    print "  - passed in foreground-color '" + enteredFGColor + "' was converted to '" + convertedFGColor + "'."
    print ""

try:
    if  len(sys.argv) == 3:
        inputdir = './input-svg'
        outputdirsvg = './output-svg'
        outputdirpng = './output-png'
        bgColorInString = '#ff0000'
        fgColorInString = '#ffffff'
        bgColorOutString = cleanup_passed_color_value(sys.argv[1])
        fgColorOutString = cleanup_passed_color_value(sys.argv[2])
        if bgColorOutString != '' and fgColorOutString != '':
            print ""
            print "Running script " + sys.argv[0]
            print " - new background-color is '" + bgColorOutString + "' (passed in as " + sys.argv[1] + ")"
            print " - new foreground-color is '" + fgColorOutString + "' (passed in as " + sys.argv[2] + ")"

            for root, dirs, files in os.walk(inputdir):
                for file in files:
                    file_basename = os.path.splitext(file)[0]
                    infullfilename=os.path.normpath(root + '/' + file)
                    fileName, fileExtension = os.path.splitext(infullfilename)
                    
                    if fileExtension == '.svg':
                        outfullfilenamesvg=os.path.normpath(outputdirsvg + '/' + file)
                        outfullfilenamepng = os.path.normpath(outputdirpng + '/' + file_basename + '.png')
                        print ""
                        print 'Processing "' + infullfilename + '"'
                        print '       ==> "' + outfullfilenamesvg + '"'
                        print '       ==> "' + outfullfilenamepng + '"'
                        if (os.path.isfile(infullfilename)):
                            f=open(infullfilename, 'r')
                            lines=f.readlines()
                            f.close()
                            f=open(outfullfilenamesvg, 'w')
                            for line in lines:
                                newline=line.replace(bgColorInString, bgColorOutString + 'temporary')
                                newline=newline.replace(fgColorInString, fgColorOutString)
                                newline=newline.replace(bgColorOutString + 'temporary', bgColorOutString)
                                f.write(newline)
                            f.close()
                            
                            os.system("inkscape -f " + outfullfilenamesvg + " -e " + outfullfilenamepng)
                            print '... done.'
                        else:
                            print '... "' + infullfilename + '" is NOT a file.'
                    else:
                        print '... "' + infullfilename + '" ignored.'
            print ""
        else:
            print_illegal_color_format_screen( sys.argv[1], sys.argv[2] , bgColorOutString, fgColorOutString )
    else:
        print_usage_info_screen()
except:
    print_usage_info_screen()
