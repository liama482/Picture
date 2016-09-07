"""
picture.py
Author: Liam
Credit: <http://www.december.com/html/spec/color>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
Lgreen = Color (0x7CFC00, 0.95)
turqo = Color (0x40E0D0, 0.99)
Orange = Color (0xFF8600, 1)
black = Color (0x000000, 0.85)
purp = Color (0x68228B, 0.6)
brn = Color (0x5C3317, 0.9)
pale = Color (0xFFFACD, 0.4)

bl_line = LineStyle(3, black)
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
brkhr = RectangleAsset(130, 32, bl_line, brn)
head = EllipseAsset(120, 100, bl_line, pale)
nose = PolygonAsset([(50,60), (75, 40), (100,60)], thinline, turqo)
#eye1
#eye2

Sprite(head, (150,140))
Sprite(brkhr, (100,10))
Sprite(nose, (75,70))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
