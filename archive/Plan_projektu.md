SYSTEMOWY PLAN PROJEKTU
FAZA 0: Bootstrap - Budowa fundamentów (1-2 dni robocze)
Cel: Stworzyć Single Source of Truth (SSoT) przed jakąkolwiek pracą nad fabułą.
Zadanie 0.1: Ekstrakcja World Bible z Zootopii
Problem: Musisz znać reguły świata, które są kanoniczne (z filmu), żeby nie halucynować szczegółów.
Rozwiązanie:
Deep research o uniwersum Zootopia (filmy 1 i 2):
Geografia miasta (dystrykty, ich charakterystyka)
Hierarchie społeczne i napięcia międzygatunkowe
Technologia dostępna w tym świecie
Instytucje (ZPD, ratusz, media)
Mininotebook z zapytaniem:
   Wyekstrahuj z dostępnych źródeł o Zootopia:   - Pełną mapę miasta z charakterystyką dystryktów   - System prawny i struktura ZPD   - Historię Night Howler incident i jego konsekwencje   - Relacje między gatunkami (prey/predator dynamics)   - Technologie (brak smartfonów, ale są tablety i hologramy?)   Sformatuj jako structured JSON/Markdown
Output: world_bible/canon/zootopia_world.md
Zadanie 0.2: Style Extraction z referencyjnych powieści
Problem: "Pisz jak autor X" nie działa bez konkretnych parametrów lingwistycznych.
Najlepsza metoda:
Option A - Jeśli masz konkretne fanfiction/powieści które Ci się podobają:
Wybierz 3-5 fragmentów (każdy ~2000 słów) reprezentujących różne style:
Scena akcji
Dialog
Introspekcja/monolog wewnętrzny
Opis lokacji
Dla każdego fragmentu użyj Claude Opus z promptem:
   Przeanalizuj ten tekst i wyekstrahuj parametry stylistyczne:      STRUKTURA ZDAŃ:   - Średnia długość zdania (word count)   - Stosunek zdań prostych do złożonych   - Użycie przecinków, średników, myślników      SŁOWNICTWO:   - Poziom formalności (potoczny / literacki / techniczny)   - Gęstość przymiotników i przysłówków   - Typowe frazy/kolokacje      NARRACJA:   - Perspektywa (I/III osoba, POV)   - Show vs Tell ratio   - Sposób wprowadzania dialogów      RYTM:   - Pacing w scenach akcji vs spokojnych   - Użycie fragmentacji/elipsy      Stwórz "Style Specification" w formacie który mogę wkleić    do system prompta dla modelu generującego tekst.
Option B - Jeśli nie masz konkretnych wzorów:
Użyj deep research do znalezienia najlepiej ocenianych Zootopia fanfiction z gatunku drama/romance/mystery i powtórz proces A.
Output: world_bible/style/style_spec.md + world_bible/style/reference_samples/
Zadanie 0.3: Character Deep Profiles
Dla każdego głównego bohatera stwórz structured profile:
Metoda - Dual agent approach:
Agent Psycholog (Claude Opus, temp 0.3):
   Na podstawie kanonicznych źródeł o [postać]:   - Jakie wydarzenie ukształtowało jej światopogląd? (The Ghost)   - Jakiego fałszywego przekonania się trzyma? (The Lie)   - Co chce osiągnąć zewnętrznie? (The Want)   - Czego naprawdę potrzebuje do szczęścia? (The Need)   - Jaki jest jej największy lęk?   - Jak reaguje na stres? (fight/flight/freeze)
Agent Lingwista (Claude Sonnet, temp 0.4):
   Przeanalizuj dialogi [postaci] z filmów/materiałów źródłowych.   Wyekstrahuj jej "voice":   - Typowe zwroty/catchphrases   - Poziom sarkazmu/humoru   - Czy używa slangu, skrótów?   - Jak reaguje emocjonalnie w dialogu (czy przerywa, czy słucha)?
Output: world_bible/characters/[name].md w ustrukturyzowanym formacie (YAML/JSON front matter + markdown)
FAZA 1: Narrative Architecture (2-3 dni)
Cel: Zamknięty, przetestowany zarys fabularny gotowy do ekspansji.
Zadanie 1.1: Three-Act Backbone
Pracujesz z Gemini 2.5 Pro (2M context) w jednej długiej konwersacji.
Workflow:
Wklejasz całą zawartość z Fazy 0 (world bible, canon z pliku)
Iteracyjnie budujesz:
   CZĘŚĆ I: [5-8 kamieni milowych]   CZĘŚĆ II: [8-12 kamieni milowych]     CZĘŚĆ III: [5-8 kamieni milowych]
Dla każdego kamienia milowego zapisujesz:
Event: Co się dzieje?
Impact on Nick: Stan emocjonalny, wiedza, lokacja
Impact on Judy: jw.
Reader knows: Co czytelnik widzi/wie
Reader suspects: Domysły które chcesz podsunąć
Hidden truth: Co jest naprawdę
Kluczowe - agent validation loop:
Po każdej iteracji (np. po zbudowaniu kamieni milowych Części I) pytasz model:
Przeanalizuj ten beat sheet pod kątem:1. Plot holes - czy są luki logiczne?2. Character consistency - czy postacie działają zgodnie z profilem?3. Pacing - czy rhythm jest zbalansowany?4. Stakes progression - czy stawka rośnie?5. Foreshadowing - czy są zasiane odpowiednie hinty?Oceń w skali 1-10 i zaproponuj poprawki.
Output: plot/master_beatsheet.md
Zadanie 1.2: Information Asymmetry Matrix
Pracujesz nadal w tej samej konwersacji Gemini (pamięta cały beat sheet).
Prompt:
Na podstawie beat sheet stwórz tabelę:| Milestone | Czytelnik WIE | Czytelnik MYŚLI | Judy WIE | Nick WIE | PRAWDA ||-----------|---------------|-----------------|----------|----------|--------|| 1.3       | Nick + Skye   | Kochanka        | jw.      | Siostra  | Siostra|| ...       |               |                 |          |          |        |Zidentyfikuj momenty gdzie:- Asymetria jest za duża (czytelnik zgubi się)- Asymetria jest za mała (będzie znudzony, bo wszystko wie)- Moment reveal jest optymalny (max napięcie)
Output: plot/information_map.md
Zadanie 1.3: Scene Breakdown
Dla każdej części osobno - rozbijasz kamienie milowe na sceny.
Metoda - template driven:
Tworzysz template sceny:
## Scena [numer]**POV:** Nick / Judy / Omniscient**Lokacja:** [gdzie]**Czas:** [kiedy względem timeline]**Obecni:** [postacie]**Cel sceny (dramatyczny):** - Główny konflikt w scenie- Turn (zmiana stanu)**Co czytelnik zobaczy:**- [event 1]- [event 2]**Co czytelnik się dowie:**- [new information]**Co pozostaje ukryte:**- [seeds for later]**Nastrój/ton:** [mroczny/tense/refleksyjny]**Zakończenie sceny:** [cliffhanger / resolution / twist]**Flashback slot:** TAK/NIE - jeśli TAK, do czego?
Prosisz model (Gemini 2.5 Pro) o wypełnienie tego dla każdego kamienia milowego.
Output: plot/act1_scenes.md, plot/act2_scenes.md, plot/act3_scenes.md
FAZA 2: Pre-Production Quality Check (1 dzień)
Cel: Walidacja przed rozpoczęciem pisania.
Zadanie 2.1: Consistency Audit
Uruchamiasz nową konwersację z Gemini 2.5 Pro:
Wklejasz CAŁOŚĆ: world bible + character profiles + beat sheet + scene breakdown
Prompt:
Jesteś consistency checkerem dla scenarzysty.Przeanalizuj całość i znajdź:1. TIMELINE ERRORS: Czy wydarzenie B może wystąpić po A?2. CHARACTER CONFLICTS: Czy postać X może wiedzieć Y w scenie Z?3. WORLD RULE VIOLATIONS: Czy event narusza reguły świata?4. MOTIVATION GAPS: Czy akcja X jest uzasadniona dla postaci Y?Lista błędów w formacie:[SEVERITY: HIGH/MEDIUM/LOW] [LOCATION] [OPIS] [SUGEROWANA POPRAWKA]
Naprawiasz błędy i zapisujesz wersję 2.0.
Zadanie 2.2: Emotional Arc Validation
Używasz Claude Opus (lepszy w emocjach):
Prompt:
Przeanalizuj łuk emocjonalny głównych postaci:Nick: [lista jego stanów emocjonalnych w każdym milestone]Judy: [jw.]Sprawdź czy:1. Progresja jest naturalna (nie ma skoków)2. Momentum jest zachowane (nie ma plateau)3. Payoff w finale jest proporcjonalny do buildup4. Wątek romantyczny jest zbalansowany (nie za szybko, nie za wolno)Oceń 1-10 + sugestie.
FAZA 3: Production Setup (pół dnia)
Cel: Przygotowanie środowiska do pisania.
Zadanie 3.1: System Prompts dla agentów
Tworzysz oddzielne pliki w prompts/system_prompts/:
writer_agent.md:
Jesteś współautorem neo-noir romantic thriller osadzonego w Zootopii.STYLE CONSTRAINTS:[wklejasz tutaj style_spec.md]WORLD RULES:[kluczowe reguły z world_bible]VOICE GUIDELINES:Nick: [parametry z character profile]Judy: [parametry]YOUR TASK:Napisz scenę zgodnie z podanym planem.POKAZUJ, nie mów (show don't tell).Dialog musi brzmieć naturalnie dla każdej postaci.Każde zdanie musi posuwać akcję lub rozwijać postać.
Analogicznie dla critic_agent.md, consistency_checker.md.
Zadanie 3.2: State Tracker Init
Tworzysz state_tracker/chapter_0_baseline.json:
{  "timestamp": "początek historii",  "characters": {    "nick": {      "location": "Zootopia, Precinct 1",      "relationships": {        "judy": "partner, romantic interest",        "skye": "[UNKNOWN TO READER]"      },      "knows": ["podstawy sprawy X"],      "emotional_state": "szczęśliwy, stabilny"    },    "judy": { ... }  },  "plot_threads": {    "main_case": "aktywna",    "nick_secret": "initiated (contact from Skye)"  }}
FAZA 4: Production Pipeline (main work)
To już jest etap pisania - ale to nie Twoje pytanie teraz.