def reparar_imagen(ruta):
    # Completa esta función
     with open(ruta, "rb") as file:
        todos_los_bytes = file.read()
        chunk = bytearray()
        for i in range(0, len(todos_los_bytes), 32):
            segmento = todos_los_bytes[i:i + min(32, abs(i - len(todos_los_bytes)))]
            bytes_segmento = bytearray(segmento)
            if bytes_segmento[0] == 1:
                #byte_arreglado = bytearray(b"1")
                #byte_arreglado = (bytes_segmento[1:16:-1])
                #a = bytes_segmento[1:17:-1]
                i = bytearray()
                for l in range(0, 16):
                    i.append(bytes_segmento[17-l])
                chunk.extend(i)
                
            if bytes_segmento[0] == 0:
                #byte_arreglado = bytearray(b"0")
                #byte_arreglado = (bytes_segmento[1:17])
                chunk.extend(bytes_segmento[1:17])
            #chunk.extend(byte_arreglado)
        with open("user_info.bmp", "wb") as file2:
            file2.write(chunk)



if __name__ == '__main__':
    try:
        reparar_imagen('imagen_danada.xyz')
        print("Contraseña reparada")
    except Exception as error:
        print(f'Error: {error}')
        print("No has podido obtener la información del Ayudante!")  