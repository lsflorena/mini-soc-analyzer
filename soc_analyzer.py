eventos = [
    {"ip": "192.168.0.10", "evento": "login_sucesso"},
    {"ip": "192.168.0.11", "evento": "login_falha"},
    {"ip": "192.168.0.11", "evento": "login_falha"},
    {"ip": "192.168.0.11", "evento": "login_falha"},
    {"ip": "10.0.0.5", "evento": "scan_porta"},
    {"ip": "10.0.0.5", "evento": "scan_porta"},
    {"ip": "172.16.0.7", "evento": "login_sucesso"},
    {"ip": "8.8.8.8", "evento": "acesso_externo"},
]

def contar_eventos(lista_eventos):
    contagem = {}
    for evento in lista_eventos:
        tipo = evento["evento"]
        if tipo in contagem:
            contagem[tipo] += 1
        else:
            contagem[tipo] = 1
    return contagem

def identificar_bruteforce(lista_eventos):
    falhas_por_ip = {}
    for evento in lista_eventos:
        if evento["evento"] == "login_falha":
            ip = evento["ip"]
            falhas_por_ip[ip] = falhas_por_ip.get(ip, 0) + 1
    suspeitos = [ip for ip, qtd in falhas_por_ip.items() if qtd >= 3]
    return suspeitos

def identificar_scanners(lista_eventos):
    scans_por_ip = {}
    for evento in lista_eventos:
        if evento["evento"] == "scan_porta":
            ip = evento["ip"]
            scans_por_ip[ip] = scans_por_ip.get(ip, 0) + 1
    suspeitos = [ip for ip, qtd in scans_por_ip.items() if qtd >= 2]
    return suspeitos

def listar_ips_unicos(lista_eventos):
    pass

def gerar_relatorio(lista_eventos):
    pass

if __name__ == "__main__":
    gerar_relatorio(eventos)