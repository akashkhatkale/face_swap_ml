def swap_n_show(img1, img2, app, swapper):
    face1 = app.get(img1)[0]
    face2 = app.get(img2)[0]

    img2_ = img2.copy()
    res_img = swapper.get(img2_, face2, face1)
        
    return res_img[:,:,::]
  
    