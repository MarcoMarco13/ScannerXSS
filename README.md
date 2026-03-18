# 🛡️ ScannerXSS - Web Spider & Vulnerability Discovery

Este é um scanner dinâmico de segurança desenvolvido em Python com Selenium. Ele automatiza o processo de **Reconhecimento (Spidering)** e **Teste de Invasão (DAST)** focado em vulnerabilidades de Cross-Site Scripting (XSS).

O projeto foi criado para demonstrar habilidades em automação de segurança, manipulação de DOM e análise de superfícies de ataque.

## 🚀 Funcionalidades

- **Spidering Automático:** Navega pelo domínio alvo encontrando links internos e mapeando novas páginas.
- **Mapeamento Dinâmico:** Identifica automaticamente campos de `input`, `search` e `textarea` em qualquer página.
- **Injeção de Payloads:** Testa múltiplos vetores de ataque (Scripts, Imagens, SVGs) para burlar filtros comuns.
- **Relatório de Achados:** Gera um arquivo `relatorio_xss.txt` com as URLs e campos vulneráveis confirmados.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Selenium WebDriver:** Para interação real com o navegador e execução de JavaScript.
- **Colorama:** Para logs detalhados e visíveis no terminal.
- **Chrome WebDriver:** Motor de renderização.

## 📋 Como Usar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
   pip install selenium colorama
Clone o repositório:

git clone [https://github.com/MarcoMarco13/ScannerXSS.git](https://github.com/MarcoMarco13/ScannerXSS.git)
Configure a URL_ALVO no script e execute:

python scanner_xss.py
