import os
import time
from multiprocessing import Pool, cpu_count
from PIL import Image, ImageFilter, ImageDraw

def processar_imagem(caminho_entrada):
    nome_arquivo = os.path.basename(caminho_entrada)
    caminho_saida = os.path.join("output", nome_arquivo)
    
    with Image.open(caminho_entrada) as img:
        # Carga matemática intensa em memória (calcula 5 filtros em sequência)
        img_modificada = img.convert("L")
        for _ in range(5):
            img_modificada = img_modificada.filter(ImageFilter.GaussianBlur(radius=20))
            img_modificada = img_modificada.filter(ImageFilter.FIND_EDGES)
            
        img_modificada.save(caminho_saida)
    return caminho_saida

def gerar_imagens_teste(qtd=30):
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    arquivos_existentes = [f for f in os.listdir("input") if f.endswith(".jpg")]
    if len(arquivos_existentes) < qtd:
        print(f"[INFO] Gerando {qtd} imagens de teste...")
        for i in range(qtd):
            img_path = os.path.join("input", f"imagem_{i+1}.jpg")
            if not os.path.exists(img_path):
                img = Image.new('RGB', (2500, 2500), color=(i*15 % 255, i*30 % 255, i*45 % 255))
                draw = ImageDraw.Draw(img)
                draw.rectangle([300, 300, 2200, 2200], fill=(255, 255, 255))
                img.save(img_path)

if __name__ == '__main__':
    gerar_imagens_teste(30)
    
    arquivos = [os.path.join("input", f) for f in os.listdir("input") if f.endswith(".jpg")][:30]
    num_cores = cpu_count()
    
    print("\n====================================================")
    print(f"[INFO] Núcleos da CPU detectados: {num_cores}")
    print(f"[INFO] Total de imagens a processar: {len(arquivos)}")
    print("====================================================\n")
    
    # 1. Execução Sequencial (1 núcleo)
    print("[1/2] Rodando modo SEQUENCIAL (1 núcleo)... Aguarde...")
    inicio_seq = time.time()
    for arq in arquivos:
        processar_imagem(arq)
    tempo_seq = time.time() - inicio_seq
    print(f"-> Tempo Sequencial: {tempo_seq:.2f} segundos\n")
    
    # 2. Execução Paralela (12 núcleos)
    print(f"[2/2] Rodando modo PARALELO ({num_cores} núcleos)...")
    inicio_par = time.time()
    with Pool(processes=num_cores) as pool:
        pool.map(processar_imagem, arquivos)
    tempo_par = time.time() - inicio_par
    print(f"-> Tempo Paralelo: {tempo_par:.2f} segundos\n")
    
    # Resultado de Speedup
    speedup = tempo_seq / tempo_par if tempo_par > 0 else 0
    print("====================================================")
    print(f"[RESULTADO] Ganho de Desempenho (Speedup): {speedup:.2f}x mais rápido!")
    print("====================================================")