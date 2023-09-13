#This is a python game that i made for my students, it's a basic game that they are able to create with the commands that they know! So don't expect anything besides really basic commands here xD

#Esse é um jogo em python que eu criei para meus alunos, é um jogo basico que eles são capazes de criar com os comandos que eles sabem! Então não espere nada alem de comando basicos aqui xD

paciencia = 0
espada = False
python = False
dragao = 100
esconder = False
Bloquear = False
turno = 0
energia = 0

print("                          @@@@@       ,@            @@@@   ")
print("                        @*      @@,   ,@         @@     @@,   ")
print("                        @*       %@   ,@        @#        @/ ")
print("                        @*       @&   ,@       /@         @@")
print("                        @@@@@@@%      ,@        @/        @#")
print("                        @*            ,@        .@&     .@&    ")
print("                        %,            ,%    @,      (&%.")

print("")

print("                          -|Insira 1 para iniciar o jogo|-")
print("__")
x = int(input())
print("--")

while (x != 1 and paciencia < 3):
  paciencia = paciencia + 1

  if (paciencia != 3):

    print("Insira 1 para iniciar o jogo.")
    print("__")
    x = int(input())
    print("--")

  if (paciencia == 3):
    print("________________________________________________________")
    print("Se você não quer jogar então não jogue, comédia.")

if (x == 1 and paciencia != 3):
  print("________________________________________________________")
  print(
    "Você se encontra perdido em uma floresta, você encontra dois caminhos, um pelo mato alto e outro seguindo o rio, qual você escolhe?"
  )
  print("-Mato alto(1) | Rio (2)-")
  print("__")
  y = int(input())
  print("--")

  while (y != 1 and y != 2 and paciencia != 3):
    paciencia = paciencia + 1

    if (paciencia != 3):
      print("________________________________________________________")
      print("-Mato alto(1) | Rio (2)-")
      print("__")
      y = int(input())
      print("--")

    if (paciencia == 3):
      print(" ")
      print("________________________________________________________")
      print(
        "Enquanto você perdia tempo um monstro a espreita aproveitou o momento de distração e o atacou, devorando a sua cabeça.... que idiota."
      )
      print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
      print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
      print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
      print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

if (y == 1 and paciencia != 3):
  print(" ")
  print("________________________________________________________")
  print("Você decidiu ir pelo mato alto...")
  print("Ao caminhar pelo mato alto uma cobra salta do mato o que você faz?!")
  print("________________________________________________________")
  print("    Y")
  print("  .-^-.")
  print(" /     \      .- ~ ~ -.")
  print("()     ()    /   _ _   `.                     _ _ _")
  print(" \_   _/    /  /     \   \                . ~  _ _  ~ .")
  print("   | |     /  /       \   \             .' .~       ~-. `.")
  print("  | |    /  /         )   )           /  /             `.`.")
  print("  \ \_ _/  /         /   /           /  /                `'")
  print("   \_ _ _.'         /   /           (  (")
  print("                    /   /             \  \"")
  print("                  /   /               \  \"")
  print("                 /   /                 )  )")
  print("                (   (                 /  /")
  print("                 `.  `.             .'  /")
  print("                    `.   ~ - - - - ~   .'")
  print("                       ~ . _ _ _ _ . ~")
  print("________________________________________________________")
  print("-Atacar(1) | Bloquear(2) | Fugir(3)")
  print("__")
  z = int(input())
  print("--")

  while (z != 1 and z != 2 and z != 3 and paciencia != 3):
    paciencia = paciencia + 1

    if (paciencia != 3):
      print("________________________________________________________")
      print("-Atacar(1) | Bloquear(2) | Fugir(3)")
      print("__")
      z = int(input())
      print("--")

    if (paciencia == 3):
      print(" ")
      print("________________________________________________________")
      print(
        "Enquanto você ponderava as razões da existência humana a cobra pula e te morde.... idiota."
      )
      print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
      print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
      print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
      print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

  if (z == 1 and paciencia != 3):
    print(" ")
    print("________________________________________________________")
    print(
      "Você ataca a cobra dando um poderoso chute que a faz voar para longe, mas não antes de ela te morder.... gênio"
    )
    print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
    print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
    print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
    print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")
    paciencia = 3

  if (z == 2 and paciencia != 3):
    print(" ")
    print("________________________________________________________")
    print(
      "Você bloqueia o ataque da cobra!...... e ela te morde... não foi uma boa ideia"
    )
    print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
    print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
    print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
    print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")
    paciencia = 3

  if (z == 3 and paciencia != 3):
    print(" ")
    print("________________________________________________________")
    print(
      "Você corre para longe do mato e acaba caindo em um buraco, quando levanta você ve um caminho atravessado por um rio aonde deveria ter uma ponte, o que você faz?"
    )
    print(" ")
    print(" _____________________________________________")
    print("|.'',        .                    *       ,''.|")
    print("|.'.'',             .                   ,''.'.|")
    print("|.'.'.'',             ,-,     .       ,''.'.'.|")
    print("|.'.'.'.'',     *    /.(            ,''.'.'.'.|")
    print("|.'.'.'.'.|          \ {  .         |.'.'.'.'.|")
    print("|.'.'.'.'.|===;       `-`       ;===|.'.'.'.'.|")
    print("|.'.'.'.'.|:::|',   *         ,'|:::|.'.'.'.'.|")
    print("|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|")
    print("|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|")
    print("|,',',',',|---|',|'|???????|'|,'|---|,',',',',|")
    print("|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|")
    print("|.'.'.'.'.|---|','   /===\   ','|---|.'.'.'.'.|")
    print("|.'.'.'.'.|===:'    /=====\    ':===|.'.'.'.'.|")
    print("|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|")
    print("|.'.'.'.','       /=========\       ','.'.'.'.|")
    print("|.'.'.','        /===========\        ','.'.'.|")
    print("|.'.','         /=============\         ','.'.|")
    print("|.','          /===============\          ','.|")
    print("|;____________/=================\____________;|")
    print("________________________________________________________")
    print("-Seguir reto(1) | Não fazer nada (2)-")
    print("__")
    c = int(input())
    print("--")

    while (c != 1 and c != 2 and paciencia != 3):

      if (paciencia != 3):
        print("________________________________________________________")
        print("-Seguir a estrada(1) | Não fazer nada (2)-")
        print("__")
        c = int(input())
        print("--")

      if (paciencia == 3):
        print("________________________________________________________")
        print(
          "Você enquanto contemplava a lua, horas se passam e você se ve cercado por caranguejos que o devoram vivo...  não seja um lunatico."
        )

        print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
        print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
        print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
        print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

    if (c == 1 and c != 3):
      print("________________________________________________________")
      print(
        "Você segue reto pelo caminho, tropeça e cai no rio se afogando e morrendo...  troxa."
      )
      print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
      print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
      print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
      print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

    if (c == 2 and c != 3):
      print("________________________________________________________")
      print(
        "Você descide parar para descansar e depois de algumas horas uma criatura sai de dentro do rio com sua parte superior semelhante a de um cavalo e a inferior a de um peixe."
      )
      print("________________________________________________________")
      print("               '-.,;;:;,")
      print("                 _;\;|\;:;,")
      print("                ) __ ' \;::,")
      print("            .--'  e   ':;;;:,           ;,")
      print("           (^           ;;::;          ;;;,")
      print("   _        --_.--.___,',:;::;     ,,,;:;;;,")
      print("  < \        `;     |  ;:;;:;        ':;:;;;,,")
      print("<`-; \__     ,;    /    ';:;;:,       ';;;'")
      print("<`_   __',   ; ,  /    ::;;;:         //")
      print("   `)|  \ \   ` .'      ';;:;,       //")
      print("   `    \ `\  /        ;;:;;.      //_")
      print("          \  `/`         ;:;  ~._,=~`   `~=,")
      print("           \_|      (        ^     ^  ^ _^  \"")
      print("            \    _,`      / ^ ^  ^   .' `.^ ;")
      print(" <`-.      '-;`       /`  ^   ^  /\    ) ^/")
      print(" <'- \__..-'` ___,,,-'._ ^  ^ _.'\^`'-' ^/")
      print("     `)_   ..-''`          `~~~~`    `~===~`")
      print("     <_.-`-._\"")
      print("________________________________________________________")
      print("-O que é você(1) | Posso montar em você?(2) | Gritar(3)-")
      print("__")
      v = int(input())
      print("--")

      while (v != 1 and v != 2 and v != 3 and paciencia != 3):

        if (paciencia != 3):
          print("________________________________________________________")
          print("-O que é você(1) | Posso montar em você?(2) | Gritar(3)-")
          print("__")
          v = int(input())
          print("--")

      if (v == 1):
        print("________________________________________________________")
        print(
          "Você pergunta para criatura o que ela é, a criatura parece ficar magoada e pula para dentro do rio desaparecendo."
        )
        print(
          "Com o choro da criatura uma lagosta colossal sai de dentro do rio e parece furiosa, ela avança na sua direção o devorando."
        )
        print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
        print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
        print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
        print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

      if (v == 2):
        print("________________________________________________________")
        print(
          "A criatura levanta as orelhas e se agaixa, parece dar permissão.")
        print("________________________________________________________")
        print("-Montar(1) | Atacar(2)-")
        print("__")
        b = int(input())
        print("--")

        while (b != 1 and b != 2 and paciencia != 3):

          if (paciencia != 3):
            print("__")
            v = int(input())
            print("--")

          if (paciencia == 3):
            print(
              "Enquanto você fazia nada você tem um ataque cardiaco e morre.")
        if (b == 1 and paciencia != 3):
          print("________________________________________________________")
          print(
            "Você monta e ela morde a sua perna o arrastando para o fundo do rio..."
          )
          print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
          print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
          print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
          print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

        if (b == 2 and paciencia != 3):
          print("________________________________________________________")
          print(
            "Você aproveita a abertura e ataca a criatura, você sobe no pescoço dela e puxa seus cabelos a direcionando para o outro lado do rio, chegando a beira você é arremeçado e a criatura foge para dentro do rio."
          )
          print("________________________________________________________")
          print(
            "Seguindo o caminho até o fim você encontra dois altares com uma reliquia em cada altar, qual você escolhe?"
          )
          print("________________________________________________________")
          print("|.'',        .                        *       ,''.|")
          print("|.'.'',             .                       ,''.'.|")
          print("|.'.'.'',                 ,-,     .       ,''.'.'.|")
          print("|.'.'.'.'',     *        /.(            ,''.'.'.'.|")
          print("|.'.'.'.'.|              \ {  .         |.'.'.'.'.|")
          print("|.'.'.'.'.|=============================|.'.'.'.'.|")
          print("|.'.'.'.'.|:::::::::::::::::::::: ::::::|.'.'.'.'.|")
          print("|.'.'.'.'.|--------------------- | -----|.'.'.'.'.|")
          print("|.'.'.'.'.|:::::::::::::::::::: _|_ ::::|.'.'.'.'.|")
          print("|,',',',',|---  _@_ ----------- _|_ ----|,',',',',|")
          print("|.'.'.'.'.|::: (   ) ::::::::: (   ) :::|.'.'.'.'.|")
          print("|.'.'.'.'.|---- ||| ----------- ||| ----|.'.'.'.'.|")
          print("|.'.'.'.'.|____ ||| ___________ ||| ____|.'.'.'.'.|")
          print("|.'.'.'.'.|____ ||| ___________ ||| ____|.'.'.'.'.|")
          print("|.'.'.'.','     ||| .           |||     ','.'.'.'.|")
          print("|.'.'.','  .   (___)       -   (___)      ','.'.'.|")
          print("|.'.','     -                  -            ','.'.|")
          print("|.','              .                   ,      ','.|")
          print("|;_______________________________________________;|")

          print("________________________________________________________")
          print("-Relíquia amarela e azul(1) | Relíquia Afiada(2)-")
          print("__")
          n = int(input())
          print("--")

          while (n != 1 and n != 2 and paciencia != 3):
            if (paciencia != 3):
              print("__")
              n = int(input())
              print("--")

            if (paciencia == 3):
              print("________________________________________________________")
              print(
                "Você ficou muito tempo admirando as reliquias e o templo se irritou, dessa forma destruindo sua alma."
              )
              print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
              print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
              print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
              print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

          if (n == 1 and paciencia != 3):
            print("________________________________________________________")
            print(
              "Você escolhe a reliquia amarela e azul, uma energia mágica envolta o seu corpo."
            )
            print("________________________________________________________")
            print(" ")
            print("                                   .::::::::::.")
            print("                                  .::``::::::::::.")
            print("                                  :::..:::::::::::")
            print("                                  ````````::::::::")
            print(
              "                          .::::::::::::::::::::::: iiiiiii,")
            print(
              "                       .:::::::::::::::::::::::::: iiiiiiiii.")
            print(
              "                       ::::::::::::::::::::::::::: iiiiiiiiii    - Você obteve uma Reliquia Mágica!"
            )
            print(
              "                       ::::::::::::::::::::::::::: iiiiiiiiii")
            print(
              "                       :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii")
            print(
              "                       :::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii")
            print(
              "                       `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`")
            print("                          `:::::: iiiiiiiiiiiiiiiiiiiiiii`")
            print("                                  iiiiiiii,,,,,,,,")
            print("                                  iiiiiiiiiii''iii")
            print("                                  `iiiiiiiiii..ii`")
            print("                                    `iiiiiiiiii")
            python = True

          if (n == 2 and paciencia != 3):
            print("________________________________________________________")
            print(
              "Você escolhe a reliquia afiada, a espada brilha e parece renovada."
            )
            print("________________________________________________________")
            print("       .-.")
            print("      {{@}}")
            print("       8@8")
            print("       888")
            print("       8@8")
            print(" _     )8(     _")
            print("(@)___/8@8\___(@)")
            print(" `~''-=):(=-''~`      == Você obteve uma espada antiga.")
            print("       |.|      ")
            print("       |S|      ")
            print("       |'|")
            print("       |.|")
            print("       |P|")
            print("       |'|")
            print("       |.|")
            print("       |U|")
            print("       |'|")
            print("       |.|")
            print("       |N|")
            print("       |'|")
            print("       |.|")
            print("       |K|")
            print("       |'|")
            print("       \ /")
            print("        ^ ")

            espada = True
          if (n == 1 or n == 2 and paciencia != 3):
            print("________________________________________________________")
            print(
              "Uma energia mágica envolta o local e as paredes descem liberando uma enorme arena aonde um feroz dragão descança."
            )

            while (dragao > 0 and paciencia != 3):
              turno = turno + 1

              if (python == True and paciencia != 3):
                if (dragao > 80):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("          /                            )")
                  print("          (                             |\"")
                  print("         /|                              \\")
                  print("        //                                \\")
                  print("       ///                                 \|")
                  print("      /( \                                  )\"")
                  print("      \\  \_                               //)")
                  print("       \\  :\__                           ///")
                  print("        \\     )                         // \"")
                  print("         \\:  /                         // |/")
                  print("          \\ / \                       //  \"")
                  print("           /)   \   ___..-'           (|  \_|")
                  print("          //     /   _.'              \ \  \"")
                  print("         /|       \ \________          \ | /")
                  print("        (| _ _  __/          '-.       ) /.'")
                  print("         \\ .  '-.__            \_    / / \"")
                  print("          \\_'.     > --._ '.     \  / / /")
                  print("           \ \      \     \  \     .' /.'")
                  print("            \ \  '._ /     \ )    / .' |")
                  print("             \ \_     \_   |    .'_/ __/")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\    /\      ) ___(    /_.'           \    |")
                  print("  | _\__// \    (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ (@)  ")
                  print("            / \          ")
                if (dragao <= 80 and dragao > 60):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("          /                            )")
                  print("          (                             |\"")
                  print("         /|                              \\")
                  print("        //                                \\")
                  print("       ///                                 \|")
                  print("      /( \                                  )\"")
                  print("      \\  \_                               //)")
                  print("       \\  :\__                           ///")
                  print("        \\     )                         // \"")
                  print("         \\:  /                         // |/")
                  print("          \\ / \                       //  \"")
                  print("           /)   \   ___..-'           (|  \_|")
                  print("          //     /   _.'              \ \  \"")
                  print("         /|       \ \________          \ | /")
                  print("        (| _ _  __/          '-.       ) /.'")
                  print("         \\ .  '-.__            \_    / / \"")
                  print("          \\_'.     > --._ '.     \  / / /")
                  print("           \ \      \     \  \     .' /.'")
                  print("            \ \  '._ /     \ )    / .' |")
                  print("             \ \_     \_   |    .'_/ __/")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ (@)  ")
                  print("            / \          ")
                if (dragao <= 60 and dragao > 40):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("                                       )")
                  print("                                        |\"")
                  print("                                         \\")
                  print("                                          \\")
                  print("                                           \|")
                  print("                                            )\"")
                  print("                                           //)")
                  print("                                          ///")
                  print("                                         // \"")
                  print("                                        // |/")
                  print("                                       //  \"")
                  print("                    ___..-'           (|  \_|")
                  print("                 /   _.'              \ \  \"")
                  print("               /    \________          \ | /")
                  print("              |            '-.       ) /.'")
                  print("              '-.__            \_    / / \"")
                  print("                    > --._ '.     \  / / /")
                  print("                          \  \     .' /.'")
                  print("             _________     \ )    / .' |")
                  print("             \ \_     \_   |    .'_/ __/")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ (@)  ")
                  print("            / \          ")
                if (dragao <= 40 and dragao > 20):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("                                       ")
                  print("                                        ")
                  print("                                         ")
                  print("                                          ")
                  print("                                           ")
                  print("                                            ")
                  print("                                           ")
                  print("                                          ")
                  print("                                         ")
                  print("                                        ")
                  print("                                       ")
                  print("                    ___..-'           ")
                  print("                 /   _.'              ")
                  print("               /    \________          ")
                  print("              |            '-.       ")
                  print("              '-.__            \_    ")
                  print("                    > --._ '.     \  ")
                  print("                          \  \     .")
                  print("             _________     \ )    / \ ")
                  print("             \ \_     \_   |    .'___\__")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ (@)  ")
                  print("            / \          ")
                if (dragao <= 20):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("                                       ")
                  print("                                        ")
                  print("                                         ")
                  print("                                          ")
                  print("                                           ")
                  print("                                            ")
                  print("                                           ")
                  print("                                          ")
                  print("                                         ")
                  print("                                        ")
                  print("                                       ")
                  print("                               ")
                  print("                               ")
                  print("                         ")
                  print("                     ")
                  print("                  ")
                  print("                      ")
                  print("                          ")
                  print("             _________       _________ ")
                  print("             \ \_     \_    /    .'___\"")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ (@)  ")
                  print("            / \          ")

              if (espada == True and paciencia != 3):
                if (dragao > 80):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("          /                            )")
                  print("          (                             |\"")
                  print("         /|                              \\")
                  print("        //                                \\")
                  print("       ///                                 \|")
                  print("      /( \                                  )\"")
                  print("      \\  \_                               //)")
                  print("       \\  :\__                           ///")
                  print("        \\     )                         // \"")
                  print("         \\:  /                         // |/")
                  print("          \\ / \                       //  \"")
                  print("           /)   \   ___..-'           (|  \_|")
                  print("          //     /   _.'              \ \  \"")
                  print("         /|       \ \________          \ | /")
                  print("        (| _ _  __/          '-.       ) /.'")
                  print("         \\ .  '-.__            \_    / / \"")
                  print("          \\_'.     > --._ '.     \  / / /")
                  print("           \ \      \     \  \     .' /.'")
                  print("            \ \  '._ /     \ )    / .' |")
                  print("             \ \_     \_   |    .'_/ __/")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\    /\      ) ___(    /_.'           \    |")
                  print("  | _\__// \    (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ -|===>  ")
                  print("            / \          ")
                if (dragao <= 80 and dragao > 60):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("          /                            )")
                  print("          (                             |\"")
                  print("         /|                              \\")
                  print("        //                                \\")
                  print("       ///                                 \|")
                  print("      /( \                                  )\"")
                  print("      \\  \_                               //)")
                  print("       \\  :\__                           ///")
                  print("        \\     )                         // \"")
                  print("         \\:  /                         // |/")
                  print("          \\ / \                       //  \"")
                  print("           /)   \   ___..-'           (|  \_|")
                  print("          //     /   _.'              \ \  \"")
                  print("         /|       \ \________          \ | /")
                  print("        (| _ _  __/          '-.       ) /.'")
                  print("         \\ .  '-.__            \_    / / \"")
                  print("          \\_'.     > --._ '.     \  / / /")
                  print("           \ \      \     \  \     .' /.'")
                  print("            \ \  '._ /     \ )    / .' |")
                  print("             \ \_     \_   |    .'_/ __/")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ -|===>  ")
                  print("            / \          ")
                if (dragao <= 60 and dragao > 40):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("                                       )")
                  print("                                        |\"")
                  print("                                         \\")
                  print("                                          \\")
                  print("                                           \|")
                  print("                                            )\"")
                  print("                                           //)")
                  print("                                          ///")
                  print("                                         // \"")
                  print("                                        // |/")
                  print("                                       //  \"")
                  print("                    ___..-'           (|  \_|")
                  print("                 /   _.'              \ \  \"")
                  print("               /    \________          \ | /")
                  print("              |            '-.       ) /.'")
                  print("              '-.__            \_    / / \"")
                  print("                    > --._ '.     \  / / /")
                  print("                          \  \     .' /.'")
                  print("             _________     \ )    / .' |")
                  print("             \ \_     \_   |    .'_/ __/")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ -|===>  ")
                  print("            / \          ")
                if (dragao <= 40 and dragao > 20):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("                                       ")
                  print("                                        ")
                  print("                                         ")
                  print("                                          ")
                  print("                                           ")
                  print("                                            ")
                  print("                                           ")
                  print("                                          ")
                  print("                                         ")
                  print("                                        ")
                  print("                                       ")
                  print("                    ___..-'           ")
                  print("                 /   _.'              ")
                  print("               /    \________          ")
                  print("              |            '-.       ")
                  print("              '-.__            \_    ")
                  print("                    > --._ '.     \  ")
                  print("                          \  \     .")
                  print("             _________     \ )    / \ ")
                  print("             \ \_     \_   |    .'___\__")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ -|===>  ")
                  print("            / \          ")
                if (dragao <= 20):
                  print("insira valor para continuar.")
                  cont = input()
                  print(
                    "________________________________________________________")
                  print(" ")
                  print("                                       ")
                  print("                                        ")
                  print("                                         ")
                  print("                                          ")
                  print("                                           ")
                  print("                                            ")
                  print("                                           ")
                  print("                                          ")
                  print("                                         ")
                  print("                                        ")
                  print("                                       ")
                  print("                               ")
                  print("                               ")
                  print("                         ")
                  print("                     ")
                  print("                  ")
                  print("                      ")
                  print("                          ")
                  print("             _________       _________ ")
                  print("             \ \_     \_    /    .'___\"")
                  print("              \  \      \_ |   / /  _/ \_")
                  print("               \  \       / _.' /  /     \"")
                  print("               \   |     /.'   / .'       '-,_")
                  print("                \   \  .'   _.'_/             \"")
                  print("   /\            ) ___(    /_.'           \    |")
                  print("  | _\_____     (.'      _/               |    |")
                  print("  \/_  __  /--'`    ,                   __/    /")
                  print("  (_ ) /b)  \  '.   :            \___.-'_/ \__/")
                  print("  /:/:  ,     ) :        (      /_.'__/-'|_ _ /")
                  print(" /:/: __/\ >  __,_.----.__\    /        (/(/(/")
                  print("(_(,_/V .'/--'    _/  __/ |   /")
                  print(" VvvV  //`    _.-' _.'     \   \"")
                  print("   n_n//     (((/->/        |   /")
                  print("   '--'         ~='          \  |")
                  print("                              | |_,,,")
                  print("                              \  \  /")
                  print("                               '.__)")
                  print("             o            ")
                  print("            /|\ -|===>  ")
                  print("            / \          ")

              if (turno == 10):
                turno = 0
              if (turno == 8 and dragao > 40):
                print("O dragão levanta a calda.")
              if (turno == 6 and dragao > 40):
                print("O dragão levanta a cabeça e seu pescoço brilha..")
              if (turno == 3 and dragao > 40):
                print("O dragão levanta as suas garras.")
              print("________________________________________________________")
              print("-Atacar(1) | Bloquear(2) | Carregar(3) | Esconder(4)-")
              k = int(input())

              while (k != 1 and k != 2 and k != 3 and k != 4
                     and paciencia != 3):

                if (paciencia != 3):
                  print(
                    "________________________________________________________")
                  print(
                    "-Atacar(1) | Bloquear(2) | Carregar(3) | Esconder(4)-")
                  k = int(input())

                if (paciencia == 3):
                  print(
                    "Enquanto você contemplava o grande dragao ele sopra uma rajada de fogo e o transforma em cinzas."
                  )

              if (k == 1 and paciencia != 3):
                if (espada == True):
                  print(
                    "Você desfere um poderoso ataque e a espada brilha em um fogo dourado, você corta o Dragão."
                  )
                  dragao = dragao - 10

                  if (dragao == 80):
                    print(
                      "________________________________________________________"
                    )
                    print("O dragão perde um chifre com o poderoso ataque.")

                  if (dragao == 60):
                    print(
                      "________________________________________________________"
                    )
                    print("O dragão perde a asa direita.")
                  if (dragao == 40):
                    print(
                      "________________________________________________________"
                    )
                    print("O dragão perde a asa esquerda.")
                  if (dragao == 30):
                    print(
                      "________________________________________________________"
                    )
                    print("O dragão perde a calda.")

                if (python == True):
                  if (energia < 2):
                    print("Você sente que não coletou energia o suficiente...")
                  if (energia >= 2):
                    print(
                      "Você desfere uma rajada de mágia de compilação desintegrando uma parte do dragão."
                    )

                    dragao = dragao - 20
                    energia = energia - 2

                    if (dragao == 80):
                      print(
                        "________________________________________________________"
                      )
                      print("O dragão tem o chifre desintegrado...")
                    if (dragao == 60):
                      print(
                        "________________________________________________________"
                      )
                      print("O dragão tem a asa direita desintegrada....")
                    if (dragao == 40):
                      print(
                        "________________________________________________________"
                      )
                      print("O dragão tem a asa esquerda desintegrada....")
                    if (dragao == 20):
                      print(
                        "________________________________________________________"
                      )
                      print("O dragão tem a calda desintegrada.....")

              if (k == 2 and paciencia != 3):
                if (turno == 3):
                  if (python == True and energia >= 1):
                    print(
                      "________________________________________________________"
                    )
                    print(
                      "Uma energia mágica o protege do ataque poderoso que o dragão desfere com suas garras."
                    )
                    energia = energia - 1
                  if (espada == True):
                    print(
                      "________________________________________________________"
                    )
                    print(
                      "Você bloqueia as garras do dragão com a sua espada.")
                if (turno != 3 and turno != 8):
                  print(
                    "________________________________________________________")
                  print("Você bloqueia... e o dragão se movimenta...")

                if (turno == 8):
                  if (python == True):
                    print(
                      "________________________________________________________"
                    )
                    print(
                      "Uma energia mágica envolta você o protegendo, você bloqueia a calda do dragão."
                    )
                    energia = energia - 1
                  if (espada == True):
                    print(
                      "________________________________________________________"
                    )
                    print("Você bloqueia a calda do dragão com maestria.")

              if (k == 3 and paciencia != 3):
                if (python == True):
                  print(
                    "________________________________________________________")
                  print(
                    "Uma poderosa energia mágica azul e amarela envolta você, você se sente energético."
                  )
                  energia = energia + 1
                if (espada == True):
                  print(
                    "________________________________________________________")
                  print(
                    "Você se concentra.... nada acontece e o dragão se prepara."
                  )

              if (k == 4 and turno != 6 and paciencia != 3):
                print(
                  "Você se esconde entre os destroços.... o dragão espera.")
              if (turno == 6 and paciencia != 3):
                if (k != 4):
                  print(
                    "________________________________________________________")
                  print(
                    "O dragão solta uma rajada de fogo poderosa, desintegrando tudo em sua frente... você vira cinzas."
                  )
                  print(
                    "  ___   __   _  _  ____         __   _  _  ____  ____ ")
                  print(
                    " / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
                  print(
                    "( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
                  print(
                    " \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")
                  paciencia = 3

                if (k == 4):
                  print(
                    "________________________________________________________")
                  print(
                    "O dragão desfere uma poderosa rajada de chamas porem você se esconde entre os destroços e sai ileso."
                  )
              if (turno == 3 and paciencia != 3):
                if (k != 2):
                  print(
                    "O dragão desce o braço desferindo um poderoso corte com as suas garras... você é despedaçado e morre."
                  )
                  print(
                    "  ___   __   _  _  ____         __   _  _  ____  ____ ")
                  print(
                    " / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
                  print(
                    "( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
                  print(
                    " \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")
                  paciencia = 3

              if (turno == 8 and paciencia != 3 and dragao > 20):
                if (k != 2):
                  print(
                    "O dragão gira com a sua calda o cortando ao meio.. você morre"
                  )
                  print(
                    "  ___   __   _  _  ____         __   _  _  ____  ____ ")
                  print(
                    " / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
                  print(
                    "( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
                  print(
                    " \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")
                  paciencia = 3

      if (v == 3):
        print("A criatura se assusta e avança na sua direção o pisoteando....")
        print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
        print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
        print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
        print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")
        paciencia = 3
if (dragao <= 0 and paciencia != 3):
  print("________________________________________________________")
  print(
    "Você corta a cabeça do dragão e uma enorme energia mágica se espalha por todo lado, você é teleportado de volta para casa!!! PARABÉNS!"
  )
  if (espada == True):
    print( "________________________________________________________")
    print("                          ")
    print("                _________       _________ ")
    print("                \ \_     \_    /    .'___\"")
    print("                 \  \      \_ |   / /  _/ \_")
    print("                  \  \       / _.' /  /     \"")
    print("                  \   |     /.'   / .'       '-,_")
    print("                *   \   \  .'   _.'_/             \"")
    print("   /\           @    ) ___(    /_.'           \    |")
    print("  | _\_____     @   (.'      _/               |    |")
    print("  \/_  __  /--| @ |`    ,                   __/    /")
    print("  (X ) /X)  \ | @ |'.   :            \___.-'_/ \__/")
    print("  /:/:  ,     | @ | :        (      /_.'__/-'|_ _ /")
    print(" /:/: __/\ >  | @ |_,_.----.__\    /        (/(/(/")
    print("(_(,_/V .'/--'  @     _/  __/ |   /")
    print(" VvvV  //`      * _.-' _.'     \   \"")
    print("   n_n//        (((/->/        |   /")
    print("   '--'            ~='          \  |")
    print("                                 | |_,,,")
    print("                                 \  \  /")
    print("                                  '.__)")
    print("             o            ")
    print("            /|\ -|===>  ")
    print("            / \          ")
  if (python == True):
    print( "________________________________________________________")
    print("                |#|         ")
    print("                |#| ________       _________ ")
    print("                |#|  \_     \_    /    .'___\"")
    print("                |#| \  \      \_ |   / /  _/ \_")
    print("                |#|  \  \       / _.' /  /     \"")
    print("                |#|   \   |     /.'   / .'       '-,_")
    print("                |#|    \   \  .'   _.'_/             \"")
    print("   /\           |#|     ) ___(    /_.'           \    |")
    print("  | _\_____     |#|    (.'      _/               |    |")
    print("  \/_  __  /--| |#|  |`    ,                   __/    /")
    print("  (X ) /X)  \ | |#|  |'.   :            \___.-'_/ \__/")
    print("  /:/:  ,     | |#|  | :        (      /_.'__/-'|_ _ /")
    print(" /:/: __/\ >  | |#|  |_,_.----.__\    /        (/(/(/")
    print("(_(,_/V .'/--'  |#|      _/  __/ |   /")
    print(" VvvV  //`      |#|  _.-' _.'     \   \"")
    print("   n_n//        |#| ((/->/        |   /")
    print("   '--'         |#|   ~='          \  |")
    print("                |#|                 | |_,,,")
    print("                |#|                  \  \  /")
    print("                |#|                  '.__)")
    print("            o  /(#)\         ")
    print("           /|\(( @ )) ")
    print("           / \ \___/     ")
    
  print(" ")
  print(" __     ______  _    _  __          _______ _   _")
  print(" \ \   / / __ \| |  | | \ \        / /_   _| \ | |")
  print("  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |")
  print("   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |")
  print("    | | | |__| | |__| |    \  /\  /   _| |_| |\  |")
  print("    |_|  \____/ \____/      \/  \/   |_____|_| \_|")
if (y == 2 and paciencia != 3):
  print(" ")
  print("________________________________________________________")
  print(
    "Você escolhe seguir rio abaixo e acaba encontrando um mago que lhe mostra um baú, ele diz que pode te mandar para casa ou abrir o bau para você."
  )
  print("________________________________________________________")
  print("              _,._      ")
  print("  .||,       /_ _\ \    | Você escolhe o baú ou a saída? |")
  print(" \.`',/      |'L'| |   /   ")
  print(" = ,. =      | -,| L    ")
  print(" / || \    ,-'\"/,'`.   ")
  print("   ||     ,'   `,,. `.  ")
  print("   ,|____,' , ,;' \| |  ")
  print("  (3|\    _/|/'   _| |  ")
  print("   ||/,-''  | >-'' _,\\ ")
  print("   ||'      ==\ ,-'  ,' ")
  print("   ||       |  V \ ,|   ")
  print("   ||       |    |` |   ")
  print("   ||       |    |   \  ")
  print("   ||       |    \    \ ")
  print("   ||       |     |    \"")
  print("   ||       |      \_,-'")
  print("   ||       |___,,--'')_\"")
  print("   ||         |_|   ccc/")
  print("   ||        ccc/       ")
  print("________________________________________________________")

  print("-Abrir Baú(1) | Ir para Casa(2)-")
  print("__")
  w = int(input())
  print("--")

  while (w != 1 and w != 2 and paciencia != 3):
    paciencia = paciencia + 1

    if (paciencia != 3):
      print("________________________________________________________")
      print("-Abrir Baú(1) | Ir para Casa(2)-")
      print("__")
      w = int(input())
      print("--")

    if (paciencia == 3):
      print(" ")
      print("________________________________________________________")
      print(
        "O mago ficou irritado pela sua indecisão e decidiu desintegra-lo.. você morre."
      )
      print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
      print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
      print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
      print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")

  if (w == 1 and paciencia != 3):
    print(" ")
    print("________________________________________________________")
    print(
      "Você decide abrir o baú, dentro dele a um papel com a seguinte frase:")
    print(
      "'Talvez o verdadeiro Baú do tesouro sejam os amigos que fizemos pelo caminho...'"
    )
    print("Escurece e você morre de hipotermia sozinho.")
    print("  ___   __   _  _  ____         __   _  _  ____  ____ ")
    print(" / __) / _\ ( \/ )(  __)       /  \ / )( \(  __)(  _ \"")
    print("( (_ \/    \/ \/ \ ) _)       (  O )\ \/ / ) _)  )   /")
    print(" \___/\_/\_/\_)(_/(____)       \__/  \__/ (____)(__\_)")
  if (w == 2 and paciencia != 3):
    print("")
    print("________________________________________________________")
    print("Você é teletransportado para casa!!! Parabéns você escapou!")
    
