from cmu_graphics import *
''' New additions inlcude ''' 
### Oop 
class Rect:
    def __init__(self, left, top, width, height, fill, border):
        self.left = left
        self.top = top 
        self.width = width
        self.height = height
        self.fill = fill
        self.border = border
        self.startX = left
        self.startY = top
        
    def __repr__(self):
        return f'Rectangle({self.width} x {self.height})'
   
    def draw(self, app):
        if (self.width, self.height) != (0,0):        
            drawRect(self.left, self.top, self.width, self.height, fill = self.fill, border = self.border)

class Circ:
    def __init__(self, x, y, r, fill, border):
        self.x = x
        self.y = y 
        self.r = r
        self.fill = fill
        self.border = border
        
    def draw(self,app):
        if self.r != 0:
            drawCircle(self.x, self.y, self.r, fill = self.fill, border = self.border)
        
class LineClass:
    def __init__(self, x1, y1, x2, y2, fill):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.fill = fill
    
    def draw(self, app):
        drawLine(self.x1, self.y1, self.x2, self.y2, fill = self.fill)

class Poly:
    def __init__(self, polyList, fill):
        self.polyList = Poly.unpack(polyList)
        self.fill = fill
        
    def draw(self,app):
        drawPolygon(*self.polyList, fill = self.fill)
        
    @staticmethod
    def unpack(L):
        newList = []
        for x,y in L:
            newList.append(x)
            newList.append(y)
        return newList

class FreeDraw:
    def __init__(self, L, fill):
        self.L = L 
        self.fill = fill

    def draw(self, app): #follow previous template implement this differently
        for i in range(len(self.L) - 1):
            current = self.L[i]
            nextItem = self.L[i +1]
            drawLine(current[0], current[1], nextItem[0], nextItem[1], fill = self.fill)
    

####



### HelperFunctions

#Drawing Fuctions
def drawCanvas(app):
    #Background
    drawRect(0, 0, app.width, app.height, fill = 'gainsboro')
    drawRect(75, 50, 605, 380, fill = 'white', border = 'black')
    drawLine(0, 50, 700, 50)
    drawLine(75, 50, 75, 450)
    drawLabel('112 Paints', 350, 25, font = 'caveat', size = 30)
    drawLabel('Fill Options', 37, 275, fill = 'black', italic = True, size = 13)
    drawShapeButtons(app)
    drawColorButtons(app)
  
def drawShapeButtons(app):
    rows =  4
    cols = 2
    width = height = 30
    for row in range(rows):
        top = 60 +  row * 40
        for col in range(cols):
            left = 5 + col * 35
            drawRect(left, top, width, height, border = 'black', fill = None)
            drawInteriorShape(app, row, col)
            if app.clickedShapeButton == True:
                if app.selectedShape != None: 
                    (selectingRow, selectingCol) = app.selectedShape
                    if (row, col) == (selectingRow, selectingCol):
                        border = 'green'
                        drawRect(left, top, width, height, border = border, fill = None)
                    else:
                        drawRect(left, top, width, height, border = 'black', fill = None)
                else: 
                        drawRect(left, top, width, height, border = 'black', fill = None)
            else:
                if app.selectedShape != None: 
                    (selectingRow, selectingCol) = app.selectedShape
                    if (row, col) == (selectingRow, selectingCol):
                        border = 'green'
                        drawRect(left, top, width, height, border = border, fill = None)
                    else:
                        drawRect(left, top, width, height, border = 'black', fill = None)
                else: 
                        drawRect(left, top, width, height, border = 'black', fill = None)                
                        
def drawInteriorShape(app, row, col):
    width = height = 20
    color = 'dimGray'
    borderColor = 'darkGray'
    r = 10
    if (row,col) == (0,0):
        drawRect(10, 65, 20, 20, fill = color, border = 'black')
    if (row, col) == (0, 1):
        drawCircle(55, 75, r, fill = color, border = 'black')
    if (row, col) == (1, 0):
        drawLine(12, 123, 28, 107, fill = color)
    if (row, col) == (1, 1):
        list = [45, 110, 62, 105, 59, 125, 50, 120]
        drawPolygon(*list, fill = color, border='black')
    if (row, col) == (2, 0):
        drawLabel('✎',20, 155, font='symbols',rotateAngle=110,size=25)
        drawLabel('112', 55,160, size = 10)

    if (row, col) == (3, 0):
        drawLabel('⇦ ',20, 195, font = 'symbols', size = 25)
        drawLabel('z', 11, 204, size = 10)
    if (row, col) == (3, 1):
        drawLabel('⇦ ',55, 195, font = 'symbols', size = 25,rotateAngle =180)
        drawLabel('y', 46, 204, size = 10)
        
def drawColorButtons(app): #Function for drawing the botom 8 
    rows =  4
    cols = 2
    width = height = 30
    for row in range(rows):
        top = 290 +  row * 40
        for col in range(cols):
            left = 5 + col * 35
            colorz = [ ['red', 'orange'], ['yellow', 'green'], ['blue', 'purple'], ['black', 'grey']]
            
            #drawing the green border based on the index the player is selecting 
            if app.selectedColor != None:
                (selectingRow, selectingCol) = app.selectedColor
                if (row, col) == (selectingRow, selectingCol):
                    border = 'green'
                    drawRect(left, top, width, height, border = border, fill = colorz[row][col])
                else:
                    drawRect(left, top, width, height, border = 'black', fill = colorz[row][col])
            else: 
                drawRect(left, top, width, height, border = 'black', fill = colorz[row][col])

def drawPolyOutline(app): #function for drawing the x's when you start clicking to create
    for x,y in app.polyList:
        if app.polyList[0] == (x,y):
            drawLabel('x', x, y, size = 10, fill = 'green')
        else:
            drawLabel('x', x, y, size = 10, fill = 'red')

def drawShapesInsideMasterList(app):
    for shape in app.masterList:
        shape.draw(app)        
        

#calculation Functions 
def distance(x0, y0, x1, y1):
    return ((y1-y0)**2 + (x1 - x0)**2)**(1/2)

def insideCanvas(app,mouseX, mouseY):
    if (75 < mouseX < 680) and (50 < mouseY < 430):
        return True 
    else: return False

def buttonHighlightingLogic(app, mouseX, mouseY):
    colorButton = getColorButton(app, mouseX, mouseY)
    shapeButton = getShapeButton(app, mouseX, mouseY)
    tool = getTool(app)

    if shapeButton != None:
        if shapeButton == app.selectedShape: #deselection of a shape logic
            if tool != 'Undo' and tool != 'Redo':
                app.selectedShape = None
        else:
            app.selectedShape = shapeButton
    if colorButton != None:
        app.selectedColor = colorButton

#Grabbing Functions
def getColorButton(app, mouseX, mouseY): #gives the (row,col) location of colorButtons
     for row in range(4):
         for col in range(2):
            leftXBoundry = 5 + 35 * (col%2) 
            rightXBoundry = 5 + (col % 2 + 1) * 35 
            
            topYBoundry = 290 + 40 * (row) 
            bottomYBoundry = 290 +  (row + 1) * 40
            
            topSquareX, topSquareY = 5, 290
            bottomSquareX, bottomSquareY = 5, 440
            
            if (topSquareX< mouseX < topSquareY) and (bottomSquareX < mouseY < bottomSquareY):
                if topYBoundry <= mouseY <= bottomYBoundry:
                    if leftXBoundry <= mouseX <= rightXBoundry:
                        app.clickedColorButton = not app.clickedColorButton
                        return (row, col)
    
def getShapeButton(app, mouseX, mouseY): #gives (row, col of shape Buttons)
    for row in range(8):
        for col in range(2):
            leftXBoundry = 5 + 35 * (col % 2) 
            rightXBoundry = 5 + (col % 2 + 1) * 35 
            
            topYBoundry = 60 + 40 * (row) 
            bottomYBoundry = 60 +  (row + 1) * 40

            topSquareX, topSquareY = 5, 60
            bottomSquareX, bottomSquareY = 5, 210
            
            if (topSquareX< mouseX < topSquareY) and (bottomSquareX < mouseY < bottomSquareY):
                if topYBoundry <= mouseY <= bottomYBoundry:
                    if leftXBoundry <= mouseX <= rightXBoundry:
                        app.clickedShapeButton = not app.clickedShapeButton
                        return (row, col)
                        
def getColor(app):#colors you want your shapes to be drawn with
    if app.selectedColor == (0,0):
        return 'red'
    elif app.selectedColor == (0,1):
        return 'orange'
    elif app.selectedColor == (1,0):
        return 'yellow'
    elif app.selectedColor == (1,1):
        return 'green'
    elif app.selectedColor == (2,0):
        return 'blue'
    elif app.selectedColor == (2,1):
        return 'purple'
    elif app.selectedColor == (3,0):
        return 'black'
    elif app.selectedColor == (3,1):
        return 'gray'

def getTool(app):
    if app.selectedShape == (0, 0): #player wants to draw a rectangle
        return 'Rectangle'
    if app.selectedShape == (0, 1): #player wants to draw a circle
        return 'Circle'
    if app.selectedShape == (1,0): #player wants to draw a Line'
        return 'Line'
    if app.selectedShape == (1,1): #player wants to draw a polygon
        return 'Polygon'
    if app.selectedShape == (2,0): #player wants to use freeDraw'
        return 'FreeDraw'
    if app.selectedShape == (3,0): #player wants to undo 
        return 'Undo'
    if app.selectedShape == (3,1): #player wants to redo 
        return 'Redo'

#Instance Creation Functions
def createShapePreview(app, mouseX, mouseY): 
    color = getColor(app)
    tool = getTool(app)
    if app.selectedShape != None:
        if tool == 'Rectangle': 
            app.currShape = Rect(mouseX, mouseY, 0, 0, fill = None, border = color)
            app.drawing = True
            app.masterList.append(app.currShape)
        
        if tool == 'Circle':
            app.currShape = Circ(mouseX, mouseY, 0, fill = None, border = color)
            app.drawing = True
            app.masterList.append(app.currShape)
            
        if tool == 'Line':
            app.currShape = LineClass(mouseX, mouseY, mouseX, mouseY, fill = color)
            app.drawing = True
            app.masterList.append(app.currShape)
            
        if tool == 'Polygon':
            if len(app.polyList) >= 3 and distance(app.polyList[0][0],app.polyList[0][1], mouseX, mouseY) < 10:
                app.currShape = Poly(app.polyList, fill = color)
                app.masterList.append(app.currShape)
                app.polyList = []
            else: 
                app.polyList.append((mouseX, mouseY))

        if tool == 'FreeDraw':
            app.freeDrawList.append((mouseX, mouseY))
            app.currShape = FreeDraw(app.freeDrawList, fill = color)
            app.drawing = True
            
def modifyShapePreview(app, mouseX, mouseY): #modify shape instances in mouseDrag
    color = getColor(app)
    tool = getTool(app)
    if insideCanvas(app,mouseX, mouseY):
        if tool == 'Rectangle':
            #recalculate the left and top before changing the width and height
            app.currShape.left = min(app.currShape.startX, mouseX)
            app.currShape.top = min(app.currShape.startY, mouseY)
            
            width = abs(app.currShape.startX - mouseX)
            height = abs(app.currShape.startY - mouseY)
            
            app.currShape.width = width + 1
            app.currShape.height = height + 1
        
        if tool == 'Circle':
        #math to bound the circle within the canvas
            
            dx, dy = mouseX - app.currShape.x, mouseY - app.currShape.y
            radius = ((dx**2) + (dy**2))**0.5
            
            left = app.currShape.x - radius
            top = app.currShape.y - radius
            right = app.currShape.x + radius
            bottom = app.currShape.y + radius
            
            if (left >= 70) and (right <= 680) and (top >= 50) and (bottom <= 430) and app.drawing == True:
                app.currShape.r = radius
        
        if tool == 'Line':
            app.currShape.x2 = mouseX
            app.currShape.y2 = mouseY
        
        if tool == 'FreeDraw':
            app.freeDrawList.append((mouseX, mouseY))
            app.masterList.append(app.currShape)

def makeFreeDrawLineInstance(app, mouseX, mouseY):
    color = getColor(app)
    shape = getTool(app)
    #Reset fd instance to allow for a new shape creation
    if shape == 'FreeDraw':
        app.freeDrawList = [] #on mouseRelease

#Undo and Redo Logic
def undo(app):
    if len(app.masterList) > 0:
        trash = app.masterList.pop()
        app.recycleBin.append(trash)
def redo(app):
    if len(app.recycleBin) > 0:
        aliveAgain = app.recycleBin.pop()
        app.masterList.append(aliveAgain)

def undoRedoButtonPress(app, mouseX, mouseY):
    tool = getTool(app)
    if tool == 'Undo':
        undo(app)
    if tool == 'Redo':
        redo(app)
###


### App animations
def onAppStart(app):
    app.height = 450
    app.width = 700
    app.canvasLeft = 0
    app.canvasRight = 700
    
    
    app.masterList = []
    app.recycleBin = []
    app.polyList = [] #tracking points for polygon creation
    app.freeDrawList = []
    app.freeDrawList = [] #create instances of freeDraw Line
    app.currShape = None #drawing shapes by modifying this 
    app.drawing = False
   
    #color changing functions 
    app.selectedShape = None
    app.selectedColor = (0,0)
    app.clickedColorButton = False
    app.clickedShapeButton = False
    
    app.stepsPerSecond = 60

def onStep(app):
    pass

def onMousePress(app, mouseX, mouseY):
    #Logic for creating Instances of shapes
    if insideCanvas(app,mouseX, mouseY):
        createShapePreview(app, mouseX, mouseY)    
    
    #Logic for selecting a new color and shape index
    buttonHighlightingLogic(app, mouseX, mouseY)
    
    #Logic for undoing and redoing on a mousePress
    undoRedoButtonPress(app, mouseX, mouseY)

    
def onMouseDrag(app, mouseX, mouseY):
    modifyShapePreview(app, mouseX, mouseY)
  

def onMouseRelease(app, mouseX, mouseY):
    makeFreeDrawLineInstance(app,mouseX, mouseY)
    if app.drawing == True and app.currShape != None:
        color = getColor(app)
        app.currShape.fill = color
        app.currShape = None
        
    
def onKeyPress(app, key):
    if key == 'z':
        undo(app)
    if key == 'y':
        redo(app)

def redrawAll(app):
    drawCanvas(app)
    drawShapesInsideMasterList(app)
    drawPolyOutline(app)

def main():
    runApp()
    
main()