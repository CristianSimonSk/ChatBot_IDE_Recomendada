#!/usr/bin/env python3
import spacy
import random
from spacy.matcher import Matcher

# Carregar o modelo de idioma
nlp = spacy.load('pt_core_news_sm')
# Inicializar o matcher
matcher = Matcher(nlp.vocab)

# Definir os padrões de correspondência
padroesSaudacao = [
    {"LOWER": {"IN": ["olá", "ola", "oi", "hey", "bom", "boa"]}},
    {"LOWER": {"IN": ["dia", "tarde", "noite"]}, "OP": "?"}, 
    {"IS_PUNCT": True, "OP": "*"}
]
padroesJavaScript = [{"TEXT": {"IN": ["JavaScript", "Javascript", "javaScript", "javascript", "java script", "Java Script"]}}]
padroesPython = [{"TEXT": {"IN": ["Python", "python"]}}]
padroesJava = [{"TEXT": {"IN": ["Java", "java"]}}]
padroesPHP = [{"TEXT": {"IN": ["PHP", "php"]}}]
padroesCsharp = [{"TEXT": {"IN": ["C#", "c#"]}}]
padroesC = [{"TEXT": {"IN": ["C", "c"]}}]
padroesTypeScript = [{"TEXT": {"IN": ["TypeScript", "typescript", "Type Script", "type script"]}}]
padroesRuby = [{"TEXT": {"IN": ["Ruby", "ruby"]}}]
padroesSwift = [{"TEXT": {"IN": ["Swift", "swift"]}}]
padroesGo = [{"TEXT": {"IN": ["Go", "go"]}}]
padroesAda = [{"TEXT": {"IN": ["Ada", "ada"]}}]
padroesVB = [{"TEXT": {"IN": ["Visual Basic", "visual basic", "VB", "vb"]}}]
padroesDart = [{"TEXT": {"IN": ["Dart", "dart"]}}]
padroesKotlin = [{"TEXT": {"IN": ["Kotlin", "kotlin"]}}]
padroesAssembly = [{"TEXT": {"IN": ["Assembly", "assembly"]}}]
padroesR = [{"TEXT": {"IN": ["R", "r"]}}]
padroesPascal = [{"TEXT": {"IN": ["Object Pascal", "object pascal", "Pascal", "pascal"]}}]
padroesShellScript = [{"TEXT": {"IN": ["Shell Script", "shell script", "Shell", "shell"]}}]
padroesProlog = [{"TEXT": {"IN": ["Prolog", "prolog"]}}]
padroesLISP = [{"TEXT": {"IN": ["LISP", "lisp"]}}]
padroesLua = [{"TEXT": {"IN": ["Lua", "lua"]}}]
padroesRust = [{"TEXT": {"IN": ["Rust", "rust"]}}]
padroesObjetos = [{"TEXT": {"IN": ["objetos", "orientação a objetos", "programação orientada a objetos"]}}]
padroesWeb = [{"TEXT": {"IN": ["web", "website", "web development"]}}]
padroesMobile = [{"TEXT": {"IN": ["mobile", "app", "mobile development"]}}]
padroesDataScience = [{"TEXT": {"IN": ["data science", "data analysis", "machine learning"]}}]
padroesDesktop = [{"TEXT": {"IN": ["desktop", "desktop application", "software"]}}]
padroesTudoBem = [
    {"LOWER": {"IN": ["tudo", "td"]}},
    {"LOWER": {"IN": ["bem", "blz"]}, "OP": "?"},
    {"IS_PUNCT": True, "OP": "*"}
]
padroesTudoCerto = [
    {"LOWER": {"IN": ["tudo", "td"]}},
    {"LOWER": {"IN": ["certo", "ok", "okk"]}, "OP": "?"},
    {"IS_PUNCT": True, "OP": "*"}
]
padroesObrigado = [{"TEXT": {"IN": ["obrigado", "obrigada", "agradecido", "grato", "grata", "valeu", "muito obrigado", "muito obrigada", "muito grato", "muito grata", "agradeço", "agradeço muito"]}}]
padroesJogos = [{"TEXT": {"IN": ["jogos", "games", "desenvolvimento de jogos", "game development"]}}]
padroesEmbarcada = [{"TEXT": {"IN": ["embarcado", "embarcada", "sistemas embarcados", "embedded systems"]}}]
padroesFrontend = [{"TEXT": {"IN": ["frontend", "front-end", "desenvolvimento frontend", "front end"]}}]
padroesBackend = [{"TEXT": {"IN": ["backend", "back-end", "desenvolvimento backend", "back end"]}}]
padroesFullstack = [{"TEXT": {"IN": ["fullstack", "full stack", "desenvolvimento fullstack"]}}]
padroesIde = [{"TEXT": {"IN": ["ide", "ambiente de desenvolvimento integrado", "editor de código", "editor integrado"]}}]

# Adicionar os padrões ao matcher
matcher.add("Saudacao", [padroesSaudacao])
matcher.add("JavaScript", [padroesJavaScript])
matcher.add("Python", [padroesPython])
matcher.add("Java", [padroesJava])
matcher.add("PHP", [padroesPHP])
matcher.add("Csharp", [padroesCsharp])
matcher.add("C", [padroesC])
matcher.add("TypeScript", [padroesTypeScript])
matcher.add("Ruby", [padroesRuby])
matcher.add("Swift", [padroesSwift])
matcher.add("Go", [padroesGo])
matcher.add("Ada", [padroesAda])
matcher.add("VisualBasic", [padroesVB])
matcher.add("Dart", [padroesDart])
matcher.add("Kotlin", [padroesKotlin])
matcher.add("Assembly", [padroesAssembly])
matcher.add("R", [padroesR])
matcher.add("ObjectPascal", [padroesPascal])
matcher.add("ShellScript", [padroesShellScript])
matcher.add("Prolog", [padroesProlog])
matcher.add("LISP", [padroesLISP])
matcher.add("Lua", [padroesLua])
matcher.add("Rust", [padroesRust])
matcher.add("Objetos", [padroesObjetos])
matcher.add("Web", [padroesWeb])
matcher.add("Mobile", [padroesMobile])
matcher.add("DataScience", [padroesDataScience])
matcher.add("Desktop", [padroesDesktop])
matcher.add("TudoBem", [padroesTudoBem])
matcher.add("TudoCerto", [padroesTudoCerto])
matcher.add("Obrigado", [padroesObrigado])
matcher.add("Jogos", [padroesJogos])
matcher.add("Embarcada", [padroesEmbarcada])
matcher.add("Frontend", [padroesFrontend])
matcher.add("Backend", [padroesBackend])
matcher.add("Fullstack", [padroesFullstack])
matcher.add("Ide", [padroesIde])

# Definir as respostas predefinidas
respostas = {
    "Saudacao": ["Olá! Como posso ajudar?", "Oi! Em que posso ser útil?", "Hey! Como posso te auxiliar?", "Bom dia! Como posso ajudar?", "Boa tarde! O que posso fazer por você?", "Boa noite! Como posso te ajudar?", "E aí! Em que posso ser útil?"],
    "JavaScript": ["Para o uso de JavaScript, a IDE recomendada é o Visual Studio Code","A IDE mais utilizada para JavaScript é o Visual Studio Code", "Possivelmente em interfaces Web com uso de JavaScript, a melhor IDE será o Visual Studio Code"],
    "Python": ["Para o uso de Python, a IDE recomendada é o PyCharm","A IDE mais utilizada para Python é o Visual Studio Code"],
    "Java" : ["Para o uso de Java, a IDE recomendada é o Eclipse", "A IDE mais utilizada para Java é o IntelliJ IDEA", "Em projetos corporativos com Java, a melhor IDE será o Eclipse"],
    "PHP" : ["Para o uso de PHP, a IDE recomendada é o PhpStorm", "A IDE mais utilizada para PHP é o Visual Studio Code", "Para projetos web em PHP, a melhor IDE será o PhpStorm"],
    "Csharp" : ["Para o uso de C#, a IDE recomendada é o Visual Studio", "A IDE mais utilizada para C# é o Visual Studio", "Em desenvolvimento de aplicativos Windows com C#, a melhor IDE será o Visual Studio"],
    "C" : ["Para o uso de C, a IDE recomendada é o Code::Blocks", "A IDE mais utilizada para C é o Code::Blocks", "Em projetos de baixo nível com C, a melhor IDE será o Code::Blocks"],
    "TypeScript" : ["Para o uso de TypeScript, a IDE recomendada é o Visual Studio Code", "A IDE mais utilizada para TypeScript é o Visual Studio Code", "Em projetos de frontend com TypeScript, a melhor IDE será o Visual Studio Code"],
    "Ruby" : ["Para o uso de Ruby, a IDE recomendada é o RubyMine", "A IDE mais utilizada para Ruby é o RubyMine", "Em desenvolvimento web com Ruby, a melhor IDE será o RubyMine"],
    "Swift" : ["Para o uso de Swift, a IDE recomendada é o Xcode", "A IDE mais utilizada para Swift é o Xcode", "Em desenvolvimento de aplicativos iOS com Swift, a melhor IDE será o Xcode"],
    "Go" : ["Para o uso de Go, a IDE recomendada é o GoLand", "A IDE mais utilizada para Go é o GoLand", "Em projetos de backend com Go, a melhor IDE será o GoLand"],
    "Ada" : ["Para o uso de Ada, a IDE recomendada é o GNAT Programming Studio (GPS)", "A IDE mais utilizada para Ada é o GNAT Programming Studio (GPS)", "Em projetos críticos com Ada, a melhor IDE será o GNAT Programming Studio (GPS)"],
    "VisualBasic" : ["Para o uso de Visual Basic, a IDE recomendada é o Visual Studio", "A IDE mais utilizada para Visual Basic é o Visual Studio", "Em projetos Windows com Visual Basic, a melhor IDE será o Visual Studio"],
    "Dart" : ["Para o uso de Dart, a IDE recomendada é o Visual Studio Code", "A IDE mais utilizada para Dart é o Visual Studio Code", "Em desenvolvimento de aplicativos multiplataforma com Dart, a melhor IDE será o Visual Studio Code"],
    "Kotlin" : ["Para o uso de Kotlin, a IDE recomendada é o IntelliJ IDEA", "A IDE mais utilizada para Kotlin é o IntelliJ IDEA", "Em projetos Android com Kotlin, a melhor IDE será o IntelliJ IDEA"],
    "Assembly" : ["Para o uso de Assembly, a IDE recomendada é o Microsoft Visual Studio", "A IDE mais utilizada para Assembly é o Microsoft Visual Studio", "Em programação de baixo nível com Assembly, a melhor IDE será o Microsoft Visual Studio"],
    "R" : ["Para o uso de R, a IDE recomendada é o RStudio", "A IDE mais utilizada para R é o RStudio", "Em análise de dados com R, a melhor IDE será o RStudio"],
    "ObjectPascal" : ["Para o uso de Object Pascal, a IDE recomendada é o Embarcadero RAD Studio", "A IDE mais utilizada para Object Pascal é o Embarcadero RAD Studio", "Em desenvolvimento Delphi com Object Pascal, a melhor IDE será o Embarcadero RAD Studio"],
    "ShellScript" : ["Para o uso de Shell Script, não é necessário uma IDE específica. Um editor de texto simples é o suficiente.", "A IDE mais utilizada para Shell Script é o Vim", "Em scripts de automação de tarefas com Shell, um editor de texto simples como o Vim será suficiente"],
    "Prolog" : ["Para o uso de Prolog, a IDE recomendada é o SWI-Prolog", "A IDE mais utilizada para Prolog é o SWI-Prolog", "Em projetos de lógica com Prolog, a melhor IDE será o SWI-Prolog"],
    "LISP" : ["Para o uso de LISP, a IDE recomendada é o Emacs", "A IDE mais utilizada para LISP é o Emacs", "Em projetos de inteligência artificial com LISP, a melhor IDE será o Emacs"],
    "Lua" : ["Para o uso de Lua, a IDE recomendada é o ZeroBrane Studio", "A IDE mais utilizada para Lua é o ZeroBrane Studio", "Em desenvolvimento de jogos com Lua, a melhor IDE será o ZeroBrane Studio"],
    "Rust" : ["Para o uso de Rust, a IDE recomendada é o Visual Studio Code", "A IDE mais utilizada para Rust é o Visual Studio Code", "Em desenvolvimento de sistemas de baixo nível com Rust, a melhor IDE será o Visual Studio Code"],
    "Objetos" : ["Se voce quer algo relacionado a orientacao a objeots, as possibilidades são: JavaScript, Python e Java são linguagens de programação que suportam programação orientada a objetos.","Python, Java e C++ são exemplos de linguagens que possuem suporte para programação orientada a objetos.","Linguagens como C#, Ruby e Swift são conhecidas por sua orientação a objetos.","Java, C++ e Python são algumas das linguagens populares que seguem o paradigma de programação orientada a objetos."],
    "Web": ["Para o desenvolvimento web, as linguagens mais populares são JavaScript, HTML e CSS.", "As principais frameworks para desenvolvimento web incluem React, Angular e Vue.js.", "Para o backend web, linguagens como Python, Node.js e Ruby são comumente usadas.", "No desenvolvimento web, é importante conhecer conceitos como RESTful APIs e bancos de dados relacionais e não relacionais."],
    "Mobile": ["Para o desenvolvimento de aplicativos móveis para iOS, a linguagem principal é o Swift.", "Para o desenvolvimento de aplicativos móveis para Android, as linguagens principais são Java e Kotlin.", "Frameworks populares para desenvolvimento mobile incluem React Native e Flutter.", "É importante conhecer os princípios de design e usabilidade em aplicativos móveis."],
    "DataScience": ["Para a análise de dados e ciência de dados, as linguagens mais populares são Python e R.", "Frameworks e bibliotecas comuns para data science incluem Pandas, NumPy e SciPy.", "É importante ter conhecimentos em estatística e machine learning para trabalhar com data science.", "Ferramentas como Jupyter Notebook são amplamente utilizadas na análise e visualização de dados."],
    "Desktop": ["Para o desenvolvimento de aplicativos desktop, linguagens como Java, C# e C++ são comumente usadas.", "Frameworks populares para desenvolvimento de interfaces desktop incluem JavaFX e Windows Forms."],
    "TudoBem" : ["Tudo ótimo! Como posso ajudar?", "Estou bem, obrigado! Em que posso ser útil para você?", "Tudo tranquilo! Como posso te auxiliar?", "Estou bem, e você? Em que posso ajudar?"],
    "TudoCerto": ["Perfeito! Como posso ser útil para você?","Ótimo! Em que posso te ajudar?","Excelente! Como posso auxiliar você?","Que bom! Em que posso ser útil?"],
    "Obrigado" : ["De nada! Estou aqui para ajudar.", "Fico feliz em poder ajudar!", "Não há de quê! Estou à disposição.", "É um prazer ajudar!", "Estou aqui para ajudar, sempre que precisar.", "Não mencione! Estou à disposição.", "Estou feliz em poder auxiliar!", "Sem problemas! Estou aqui para ajudar.", "É um prazer poder ajudar!", "Estou à disposição para qualquer outra dúvida ou solicitação."],
    "Jogos": ["Para o desenvolvimento de jogos, você pode utilizar linguagens como C++, C#, Java ou Python, além de frameworks populares como Unity ou Unreal Engine."],
    "Embarcada": ["Para programação embarcada, linguagens como C e C++ são amplamente utilizadas, especialmente em microcontroladores e dispositivos IoT (Internet of Things)."],
    "Frontend": ["No desenvolvimento frontend, você pode utilizar linguagens como HTML, CSS e JavaScript, juntamente com frameworks populares como React, Angular ou Vue.js."],
    "Backend": ["No desenvolvimento backend, você pode utilizar linguagens como Python, Java, C# ou Node.js, juntamente com frameworks como Django, Spring, ASP.NET ou Express.js."],
    "Fullstack": ["No desenvolvimento fullstack, você precisa dominar tanto o frontend quanto o backend. É comum utilizar uma combinação de linguagens como HTML, CSS, JavaScript, Python, Java, C# ou Node.js, juntamente com frameworks como React, Angular, Vue.js, Django, Spring, ASP.NET ou Express.js."],
    "Ide": ["As IDEs (Integrated Development Environments) são ferramentas que auxiliam no desenvolvimento de software. Algumas IDEs populares são o Visual Studio Code, PyCharm, IntelliJ IDEA, Eclipse, Xcode, Android Studio, entre outras."],
    "default": ["Desculpe, não consegui compreender. Talvez você possa fazer uma pergunta relacionada a IDEs e linguagens de programação?","Parece que não consegui entender sua mensagem. Que tal fazer uma pergunta sobre IDEs ou linguagens de programação?","Desculpe, não consegui compreender completamente. Você tem alguma pergunta relacionada a IDEs ou linguagens de programação?","Peço desculpas pela minha falta de compreensão. Seria possível fazer uma pergunta sobre IDEs ou linguagens de programação?","Me desculpe, não consegui entender sua mensagem. Talvez você possa fazer uma pergunta sobre IDEs ou linguagens de programação?","Não consegui compreender o que você disse. Que tal fazer uma pergunta sobre IDEs ou linguagens de programação?","Desculpe, não consegui entender completamente. Você tem alguma pergunta sobre IDEs ou linguagens de programação?","Parece que não consegui compreender sua mensagem. Que tal perguntar algo relacionado a IDEs ou linguagens de programação?","Peço desculpas pela minha falta de compreensão. Seria possível fazer uma pergunta sobre IDEs ou linguagens de programação?","Me desculpe, não consegui entender sua mensagem. Que tal perguntar algo relacionado a IDEs ou linguagens de programação?"]
}

def processar_mensagem(mensagem):
    doc = nlp(mensagem.lower())

    matches = matcher(doc)
    for match_id, start, end in matches:
        padrao = nlp.vocab.strings[match_id]
        if padrao in respostas:
            return random.choice(respostas[padrao])

    return random.choice(respostas["default"])

with open("MensagemUser.txt", "r", encoding="utf-8") as arquivo_user:
    user_message = arquivo_user.read()


# Processar a mensagem e obter a resposta do bot
bot_message = processar_mensagem(user_message) #processar_mensagem(user_message)

# Sobrescrever todo o conteúdo do arquivo MensagemBot.txt com a resposta
with open("MensagemBot.txt", "w", encoding="utf-8") as arquivo_bot:
    arquivo_bot.write(bot_message)
