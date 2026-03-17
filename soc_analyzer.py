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
    ips = set()
    for evento in lista_eventos:
        ips.add(evento["ip"])
    return sorted(ips)

def gerar_relatorio(lista_eventos):
    print("=== MINI SOC ANALYZER ===")
    print()
    print(f"Total de eventos analisados: {len(lista_eventos)}")
    print()

    resumo = contar_eventos(lista_eventos)
    print("Resumo por tipo:")
    for tipo in sorted(resumo.keys()):
        print(f"{tipo}: {resumo[tipo]}")
    print()

    ips = listar_ips_unicos(lista_eventos)
    print("IPs únicos monitorados:")
    for ip in ips:
        print(ip)
    print()

    brute = identificar_bruteforce(lista_eventos)
    print("Possível brute force:")
    if brute:
        for ip in brute:
            print(ip)
    else:
        print("Nenhum")
    print()

    scanner = identificar_scanners(lista_eventos)
    print("Possível scanner:")
    if scanner:
        for ip in scanner:
            print(ip)
    else:
        print("Nenhum")

if __name__ == "__main__":
    gerar_relatorio(eventos)