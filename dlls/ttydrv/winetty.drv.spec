# GDI driver

@ cdecl Arc(ptr long long long long long long long long) TTYDRV_DC_Arc
@ cdecl BitBlt(ptr long long long long ptr long long long) TTYDRV_DC_BitBlt
@ cdecl Chord(ptr long long long long long long long long) TTYDRV_DC_Chord
@ cdecl CreateDC(long ptr wstr wstr wstr ptr) TTYDRV_DC_CreateDC
@ cdecl DeleteDC(ptr) TTYDRV_DC_DeleteDC
@ cdecl Ellipse(ptr long long long long) TTYDRV_DC_Ellipse
@ cdecl ExtEscape(ptr long long ptr long ptr) TTYDRV_ExtEscape
@ cdecl ExtFloodFill(ptr long long long long) TTYDRV_DC_ExtFloodFill
@ cdecl ExtTextOut(ptr long long long ptr ptr long ptr) TTYDRV_DC_ExtTextOut
@ cdecl GetBitmapBits(long ptr long) TTYDRV_GetBitmapBits
@ cdecl GetCharWidth(ptr long long ptr) TTYDRV_DC_GetCharWidth
@ cdecl GetDCOrgEx(ptr ptr) TTYDRV_GetDCOrgEx
@ cdecl GetDeviceCaps(ptr long) TTYDRV_GetDeviceCaps
@ cdecl GetPixel(ptr long long) TTYDRV_DC_GetPixel
@ cdecl GetSystemPaletteEntries(ptr long long ptr) TTYDRV_GetSystemPaletteEntries
@ cdecl GetTextExtentPoint(ptr ptr long ptr) TTYDRV_DC_GetTextExtentPoint
@ cdecl GetTextMetrics(ptr ptr) TTYDRV_DC_GetTextMetrics
@ cdecl LineTo(ptr long long) TTYDRV_DC_LineTo
@ cdecl PaintRgn(ptr long) TTYDRV_DC_PaintRgn
@ cdecl PatBlt(ptr long long long long long) TTYDRV_DC_PatBlt
@ cdecl Pie(ptr long long long long long long long long) TTYDRV_DC_Pie
@ cdecl PolyPolygon(ptr ptr ptr long) TTYDRV_DC_PolyPolygon
@ cdecl PolyPolyline(ptr ptr ptr long) TTYDRV_DC_PolyPolyline
@ cdecl Polygon(ptr ptr long) TTYDRV_DC_Polygon
@ cdecl Polyline(ptr ptr long) TTYDRV_DC_Polyline
@ cdecl Rectangle(ptr long long long long) TTYDRV_DC_Rectangle
@ cdecl RoundRect(ptr long long long long long long) TTYDRV_DC_RoundRect
@ cdecl SelectFont(ptr long long) TTYDRV_SelectFont
@ cdecl SetBitmapBits(long ptr long) TTYDRV_SetBitmapBits
@ cdecl SetDCOrg(ptr long long) TTYDRV_SetDCOrg
@ cdecl SetDIBitsToDevice(ptr long long long long long long long long ptr ptr long) TTYDRV_DC_SetDIBitsToDevice
@ cdecl SetPixel(ptr long long long) TTYDRV_DC_SetPixel
@ cdecl StretchBlt(ptr long long long long ptr long long long long long) TTYDRV_DC_StretchBlt

# USER driver

@ cdecl CreateDesktopWindow(long) TTYDRV_CreateDesktopWindow
@ cdecl CreateWindow(long ptr long) TTYDRV_CreateWindow
@ cdecl DestroyWindow(long) TTYDRV_DestroyWindow
@ cdecl GetDC(long long long long) TTYDRV_GetDC
@ cdecl SetWindowPos(ptr) TTYDRV_SetWindowPos
@ cdecl ShowWindow(long long) TTYDRV_ShowWindow
