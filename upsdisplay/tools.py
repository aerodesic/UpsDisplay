#
# Some useful functions
#
import wx

def scale_bitmap(bitmap, newsize):
    image = bitmap.ConvertToImage()
    image = image.Scale(newsize.GetWidth(), newsize.GetHeight(), wx.IMAGE_QUALITY_HIGH)
    return wx.Bitmap(image)

    # return wx.Bitmap(bitmap.ConvertToImage().Scale(newsize.GetWidth, newsize.GetHeight(), wx.IMAGE_QUALITY_HIGH))
