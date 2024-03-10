import cv2

def sobrepor_imagens(imagem_fundo, imagem_overlay, x, y):
    regiao_overlay = imagem_overlay[:,:,:3]  
    alpha = imagem_overlay[:,:,3] / 255.0 
    area_sobreposicao = imagem_fundo[y:y+regiao_overlay.shape[0], x:x+regiao_overlay.shape[1]]

    for c in range(0, 3):
        area_sobreposicao[:, :, c] = (1 - alpha) * area_sobreposicao[:, :, c] + alpha * regiao_overlay[:, :, c]

    return imagem_fundo

def sobrepor():
    img_fundo = cv2.imread(f"img/cache/shirt.png")
    img_overlay = cv2.imread("img/template.png", cv2.IMREAD_UNCHANGED) 

    if img_fundo is None or img_overlay is None:
        print("Deu problema")
    else:
        img_fundo = cv2.resize(img_fundo, (585, 559))
        img_overlay = cv2.resize(img_overlay, (585, 559))

        resultado = sobrepor_imagens(img_fundo.copy(), img_overlay, 0, 0)
        
        cv2.imwrite("img/result/name.png", resultado)
