stopwords_list = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "a's",
        "able",
        "about",
        "above",
        "according",
        "accordingly",
        "across",
        "actually",
        "after",
        "afterwards",
        "again",
        "against",
        "ain't",
        "all",
        "allow",
        "allows",
        "almost",
        "alone",
        "along",
        "already",
        "also",
        "although",
        "always",
        "am",
        "among",
        "amongst",
        "an",
        "and",
        "another",
        "any",
        "anybody",
        "anyhow",
        "anyone",
        "anything",
        "anyway",
        "anyways",
        "anywhere",
        "apart",
        "appear",
"appreciate",
"appropriate",
"are",
"aren't",
"around",
"as",
"aside",
"ask",
"asking",
"associated",
"at",
"available",
"away",
"awfully",
"b",
"back",
"be",
"became",
"because",
"become",
"becomes",
"becoming",
"been",
"before",
"beforehand",
"behind",
"being",
"believe",
"below",
"beside",
"besides",
"best",
"better",
"between",
"beyond",
"both",
"brief",
"but",
"by",
"bye",
"c'mon",
"c's",
"came",
"can",
"can't",
"cannot",
"cant",
"case",
"cause",
"causes",
"certain",
"certainly",
"changes",
"clearly",
"come",
"comes",
"concerning",
"consequently",
"consider",
"considering",
"consist",
"contain",
"containing",
"contains",
"corresponding",
"could",
"couldn't",
"course",
"currently",
"d",
"definitely",
"described",
"despite",
"did",
"didn't",
"different",
"do",
"does",
"doesn't",
"doing",
"don't",
"done",
"down",
"downwards",
"during",
"e",
"each",
"early",
"edu",
"eight",
"either",
"else",
"elsewhere",
"end",
"enough",
"entirely",
"especially",
"etc",
"even",
"ever",
"every",
"everybody",
"everyone",
"everything",
"everywhere",
"exactly",
"example",
"except",
"f",
"fact",
"far",
"few",
"fifth",
"first",
"five",
"follow",
"followed",
"following",
"follows",
"for",
"former",
"formerly",
"forth",
"four",
"from",
"full",
"further",
"furthermore",
"g",
"general",
"get",
"getting",
"give",
"given",
"gives",
"go",
"goes",
"going",
"gone",
"good",
"got",
"gotten",
"great",
"greetings",
"h",
"had",
"hadn't",
"happens",
"hardly",
"has",
"hasn't",
"have",
"haven't",
"having",
"he",
"he's",
"hello",
"help",
"hence",
"her",
"here",
"here's",
"hereafter",
"hereby",
"herein",
"hereupon",
"hers",
"herself",
"hi",
"high",
"him",
"himself",
"his",
"hither",
"hopefully",
"how",
"howbeit",
"however",
"i",
"i'd",
"i'll",
"i'm",
"i've",
"ie",
"if",
"ignored",
"immediate",
"important",
"in",
"inasmuch",
"inc",
"indeed",
"indicate",
"indicated",
"indicates",
"inner",
"insofar",
"instead",
"interest",
"into",
"inward",
"is",
"isn't",
"it",
"it'd",
"it'll",
"it's",
"its",
"itself",
"j",
"just",
"k",
"keep",
"keeps",
"kept",
"kind",
"knew",
"know",
"known",
"knows",
"l",
"large",
"larger",
"last",
"lately",
"later",
"latest",
"latter",
"latterly",
"least",
"lest",
"let",
"let's",
"like",
"liked",
"likely",
"little",
"long",
"longer",
"looking",
"looks",
"ltd",
"m",
"made",
"mainly",
"many",
"may",
"maybe",
"me",
"mean",
"meanwhile",
"merely",
"might",
"moreover",
"most",
"mostly",
"much",
"must",
"my",
"myself",
"n",
"name",
"namely",
"names",
"nd",
"near",
"nearly",
"necessary",
"need",
"needs",
"neither",
"never",
"nevertheless",
"new",
"next",
"nine",
"no",
"nobody",
"non",
"none",
"noone",
"nor",
"normally",
"not",
"nothing",
"novel",
"now",
"nowhere",
"o",
"obviously",
"of",
"off",
"often",
"oh",
"ok",
"okay",
"old",
"older",
"on",
"once",
"one",
"ones",
"only",
"onto",
"or",
"order",
"other",
"others",
"otherwise",
"ought",
"our",
"ours",
"ourselves",
"out",
"outside",
"over",
"overall",
"own",
"p",
"part",
"particular",
"particularly",
"per",
"perhaps",
"placed",
"please",
"plus",
"possible",
"present",
"presumably",
"probably",
"problem",
"provides",
"q",
"que",
"quite",
"qv",
"r",
"rather",
"rd",
"really",
"reasonably",
"regarding",
"regardless",
"regards",
"relatively",
"respectively",
"right",
"room",
"s",
"said",
"same",
"saw",
"say",
"saying",
"says",
"second",
"secondly",
"see",
"seeing",
"seem",
"seemed",
"seeming",
"seems",
"seen",
"sees",
"self",
"selves",
"sensible",
"sent",
"serious",
"seriously",
"seven",
"several",
"shall",
"she",
"should",
"shouldn't",
"side",
"sides",
"since",
"six",
"small",
"smaller",
"so",
"some",
"somebody",
"somehow",
"someone",
"something",
"sometime",
"sometimes",
"somewhat",
"somewhere",
"soon",
"sorry",
"specified",
"specify",
"specifying",
"state",
"states",
"still",
"sub",
"such",
"sure",
"t",
"t's",
"take",
"taken",
"tell",
"tends",
"th",
"than",
"thank",
"thanks",
"thanx",
"that",
"that's",
"thats",
"the",
"their",
"theirs",
"them",
"themselves",
"then",
"thence",
"there",
"there's",
"thereafter",
"thereby",
"therefore",
"therein",
"theres",
"thereupon",
"these",
"they",
"they'd",
"they'll",
"they're",
"they've",
"thing",
"think",
"thinks",
"third",
"this",
"thorough",
"thoroughly",
"those",
"though",
"three",
"through",
"throughout",
"thru",
"thus",
"to",
"together",
"too",
"took",
"toward",
"towards",
"tried",
"tries",
"truly",
"try",
"trying",
"turn",
"twice",
"two",
"u",
"un",
"under",
"unfortunately",
"unless",
"unlikely",
"until",
"unto",
"up",
"upon",
"us",
"use",
"used",
"useful",
"uses",
"using",
"usually",
"v",
"value",
"various",
"very",
"via",
"viz",
"vs",
"w",
"want",
"wanted",
"wants",
"was",
"wasn't",
"way",
"ways",
"we",
"we'd",
"we'll",
"we're",
"we've",
"welcome",
"well",
"went",
"were",
"weren't",
"what",
"what's",
"whatever",
"when",
"whence",
"whenever",
"where",
"where's",
"whereafter",
"whereas",
"whereby",
"wherein",
"whereupon",
"wherever",
"whether",
"while",
"whither",
"who's",
"whoever",
"whole",
"whom",
"whose",
"why",
"will",
"willing",
"wish",
"with",
"within",
"without",
"won't",
"wonder",
"work",
"would",
"wouldn't",
"x",
"y",
"year",
"yet",
"you",
"you'd",
"you'll",
"you're",
"you've",
"your",
"yours",
"yourself",
"yourselves",
"z"
]

stopwords = set(stopwords_list)
