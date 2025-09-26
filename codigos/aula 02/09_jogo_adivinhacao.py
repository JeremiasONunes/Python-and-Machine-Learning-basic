# Aula 02 - Desafio: Jogo de Adivinhação
# Jogo que usa todas as estruturas aprendidas (condicionais, while, validações)

import random

print("=== JOGO DE ADIVINHAÇÃO DE NÚMEROS ===\n")

def jogar_adivinhacao():
    # Configurações do jogo
    numero_secreto = random.randint(1, 100)
    tentativas_maximas = 7
    tentativas_usadas = 0
    pontuacao = 1000
    
    print("🎯 Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100")
    print(f"Você tem {tentativas_maximas} tentativas")
    print("Pontuação inicial: 1000 pontos\n")
    
    # Loop principal do jogo
    while tentativas_usadas < tentativas_maximas:
        tentativas_restantes = tentativas_maximas - tentativas_usadas
        
        print(f"Tentativa {tentativas_usadas + 1}/{tentativas_maximas}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Pontuação atual: {pontuacao}")
        
        # Validação da entrada
        while True:
            try:
                palpite = int(input("Digite seu palpite (1-100): "))
                if 1 <= palpite <= 100:
                    break
                else:
                    print("❌ Número deve estar entre 1 e 100!")
            except ValueError:
                print("❌ Digite apenas números!")
        
        tentativas_usadas += 1
        
        # Verifica o palpite
        if palpite == numero_secreto:
            print(f"\n🎉 PARABÉNS! Você acertou!")
            print(f"O número era {numero_secreto}")
            print(f"Tentativas usadas: {tentativas_usadas}")
            print(f"Pontuação final: {pontuacao}")
            
            # Classificação da performance
            if tentativas_usadas <= 3:
                classificacao = "EXCELENTE"
            elif tentativas_usadas <= 5:
                classificacao = "BOM"
            else:
                classificacao = "REGULAR"
            
            print(f"Performance: {classificacao}")
            return True
        
        elif palpite < numero_secreto:
            print("📈 Muito baixo! Tente um número maior.")
            dica = "maior"
        else:
            print("📉 Muito alto! Tente um número menor.")
            dica = "menor"
        
        # Reduz pontuação
        pontuacao -= 100
        
        # Dicas especiais baseadas na proximidade
        diferenca = abs(palpite - numero_secreto)
        if diferenca <= 5:
            print("🔥 Você está muito perto!")
        elif diferenca <= 15:
            print("🌡️ Você está próximo!")
        elif diferenca <= 30:
            print("🌊 Você está morno...")
        else:
            print("🧊 Você está frio!")
        
        print("-" * 40)
    
    # Fim do jogo - tentativas esgotadas
    print(f"\n💔 Game Over!")
    print(f"O número era {numero_secreto}")
    print(f"Você usou todas as {tentativas_maximas} tentativas")
    return False

def menu_principal():
    """Menu principal do jogo"""
    vitorias = 0
    derrotas = 0
    
    while True:
        print("\n" + "="*50)
        print("           JOGO DE ADIVINHAÇÃO")
        print("="*50)
        print("1. Jogar")
        print("2. Ver estatísticas")
        print("3. Como jogar")
        print("4. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            print("\n🎮 Iniciando novo jogo...")
            if jogar_adivinhacao():
                vitorias += 1
            else:
                derrotas += 1
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "2":
            total_jogos = vitorias + derrotas
            print(f"\n📊 ESTATÍSTICAS:")
            print(f"Jogos jogados: {total_jogos}")
            print(f"Vitórias: {vitorias}")
            print(f"Derrotas: {derrotas}")
            
            if total_jogos > 0:
                taxa_vitoria = (vitorias / total_jogos) * 100
                print(f"Taxa de vitória: {taxa_vitoria:.1f}%")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":
            print(f"\n📖 COMO JOGAR:")
            print("• O computador escolhe um número entre 1 e 100")
            print("• Você tem 7 tentativas para adivinhar")
            print("• A cada palpite, recebe dicas se o número é maior ou menor")
            print("• Sua pontuação diminui a cada tentativa errada")
            print("• Quanto menos tentativas usar, melhor sua classificação!")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "4":
            print("\n👋 Obrigado por jogar!")
            print("Até a próxima!")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")

# Inicia o jogo
if __name__ == "__main__":
    menu_principal()