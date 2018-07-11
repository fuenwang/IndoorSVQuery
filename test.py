from GoogleSVLibrary import StreetViewInfo
from GoogleSVLibrary import StreetViewImage
from GoogleSVLibrary import StreetViewDepth

panoid = 'AF1QipNSTzNoyp9MIPJq0NJbpwH5qsW-MIPOqBq7TMzj'

StreetViewImage.GetPanoByID_full(panoid[len(panoid)-22:], './')
