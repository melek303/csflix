import json

results1= [
    {
      "adult": False,
      "backdrop_path": "/fqv8v6AycXKsivp1T5yKtLbGXce.jpg",
      "genre_ids": [
        878,
        12,
        28
      ],
      "id": 653346,
      "original_language": "en",
      "original_title": "Kingdom of the Planet of the Apes",
      "overview": "Several generations in the future following Caesar's reign, apes are now the dominant species and live harmoniously while humans have been reduced to living in the shadows. As a new tyrannical ape leader builds his empire, one young ape undertakes a harrowing journey that will cause him to question all that he has known about the past and to make choices that will define a future for apes and humans alike.",
      "popularity": 6097.733,
      "poster_path": "/gKkl37BQuKTanygYQG1pyYgLVgf.jpg",
      "release_date": "2024-05-08",
      "title": "Kingdom of the Planet of the Apes",
      "video": False,
      "vote_average": 6.926,
      "vote_count": 787
    },
    {
      "adult": False,
      "backdrop_path": "/z121dSTR7PY9KxKuvwiIFSYW8cf.jpg",
      "genre_ids": [
        10752,
        28,
        18
      ],
      "id": 929590,
      "original_language": "en",
      "original_title": "Civil War",
      "overview": "In the near future, a group of war journalists attempt to survive while reporting the truth as the United States stands on the brink of civil war.",
      "popularity": 3038.92,
      "poster_path": "/sh7Rg8Er3tFcN9BpKIPOMvALgZd.jpg",
      "release_date": "2024-04-10",
      "title": "Civil War",
      "video": False,
      "vote_average": 7.08,
      "vote_count": 1249
    },
    {
      "adult": False,
      "backdrop_path": "/xRd1eJIDe7JHO5u4gtEYwGn5wtf.jpg",
      "genre_ids": [
        878,
        28,
        12
      ],
      "id": 823464,
      "original_language": "en",
      "original_title": "Godzilla x Kong: The New Empire",
      "overview": "Following their explosive showdown, Godzilla and Kong must reunite against a colossal undiscovered threat hidden within our world, challenging their very existence – and our own.",
      "popularity": 2176.392,
      "poster_path": "/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg",
      "release_date": "2024-03-27",
      "title": "Godzilla x Kong: The New Empire",
      "video": False,
      "vote_average": 7.238,
      "vote_count": 2478
    },
    {
      "adult": False,
      "backdrop_path": "/otfoeC96neoOdA4HqsX06OWuzE9.jpg",
      "genre_ids": [
        27,
        53
      ],
      "id": 719221,
      "original_language": "en",
      "original_title": "Tarot",
      "overview": "When a group of friends recklessly violate the sacred rule of Tarot readings, they unknowingly unleash an unspeakable evil trapped within the cursed cards. One by one, they come face to face with fate and end up in a race against death.",
      "popularity": 2131.33,
      "poster_path": "/gAEUXC37vl1SnM7PXsHTF23I2vq.jpg",
      "release_date": "2024-05-01",
      "title": "Tarot",
      "video": False,
      "vote_average": 6.484,
      "vote_count": 313
    },
    {
      "adult": False,
      "backdrop_path": "/3TNSoa0UHGEzEz5ndXGjJVKo8RJ.jpg",
      "genre_ids": [
        878,
        28
      ],
      "id": 614933,
      "original_language": "en",
      "original_title": "Atlas",
      "overview": "A brilliant counterterrorism analyst with a deep distrust of AI discovers it might be her only hope when a mission to capture a renegade robot goes awry.",
      "popularity": 1821.917,
      "poster_path": "/bcM2Tl5HlsvPBnL8DKP9Ie6vU4r.jpg",
      "release_date": "2024-05-23",
      "title": "Atlas",
      "video": False,
      "vote_average": 6.7,
      "vote_count": 563
    },
    {
      "adult": False,
      "backdrop_path": "/H5HjE7Xb9N09rbWn1zBfxgI8uz.jpg",
      "genre_ids": [
        28,
        35,
        80,
        9648,
        10749
      ],
      "id": 746036,
      "original_language": "en",
      "original_title": "The Fall Guy",
      "overview": "Fresh off an almost career-ending accident, stuntman Colt Seavers has to track down a missing movie star, solve a conspiracy and try to win back the love of his life while still doing his day job.",
      "popularity": 1217.797,
      "poster_path": "/tSz1qsmSJon0rqjHBxXZmrotuse.jpg",
      "release_date": "2024-04-24",
      "title": "The Fall Guy",
      "video": False,
      "vote_average": 7.283,
      "vote_count": 1000
    },
    {
      "adult": False,
      "backdrop_path": "/fY3lD0jM5AoHJMunjGWqJ0hRteI.jpg",
      "genre_ids": [
        878,
        27,
        28
      ],
      "id": 940721,
      "original_language": "ja",
      "original_title": "ゴジラ-1.0",
      "overview": "In postwar Japan, Godzilla brings new devastation to an already scorched landscape. With no military intervention or government help in sight, the survivors must join together in the face of despair and fight back against an unrelenting horror.",
      "popularity": 1209.099,
      "poster_path": "/hkxxMIGaiCTmrEArK7J56JTKUlB.jpg",
      "release_date": "2023-11-03",
      "title": "Godzilla Minus One",
      "video": False,
      "vote_average": 7.664,
      "vote_count": 1435
    },
    {
      "adult": False,
      "backdrop_path": "/tkHQ7tnYYUEnqlrKuhufIsSVToU.jpg",
      "genre_ids": [
        27
      ],
      "id": 437342,
      "original_language": "en",
      "original_title": "The First Omen",
      "overview": "When a young American woman is sent to Rome to begin a life of service to the church, she encounters a darkness that causes her to question her own faith and uncovers a terrifying conspiracy that hopes to bring about the birth of evil incarnate.",
      "popularity": 1127.216,
      "poster_path": "/uGyiewQnDHPuiHN9V4k2t9QBPnh.jpg",
      "release_date": "2024-04-03",
      "title": "The First Omen",
      "video": False,
      "vote_average": 6.831,
      "vote_count": 364
    },
    {
      "adult": False,
      "backdrop_path": "/shrwC6U8Bkst9T9J7fr1A50n6x6.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 786892,
      "original_language": "en",
      "original_title": "Furiosa: A Mad Max Saga",
      "overview": "As the world fell, young Furiosa is snatched from the Green Place of Many Mothers and falls into the hands of a great Biker Horde led by the Warlord Dementus. Sweeping through the Wasteland they come across the Citadel presided over by The Immortan Joe. While the two Tyrants war for dominance, Furiosa must survive many trials as she puts together the means to find her way home.",
      "popularity": 1055.646,
      "poster_path": "/iADOJ8Zymht2JPMoy3R7xceZprc.jpg",
      "release_date": "2024-05-22",
      "title": "Furiosa: A Mad Max Saga",
      "video": False,
      "vote_average": 7.722,
      "vote_count": 681
    },
    {
      "adult": False,
      "backdrop_path": "/xOMo8BRK7PfcJv9JCnx7s5hj0PX.jpg",
      "genre_ids": [
        878,
        12
      ],
      "id": 693134,
      "original_language": "en",
      "original_title": "Dune: Part Two",
      "overview": "Follow the mythic journey of Paul Atreides as he unites with Chani and the Fremen while on a path of revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the known universe, Paul endeavors to prevent a terrible future only he can foresee.",
      "popularity": 897.168,
      "poster_path": "/czembW0Rk1Ke7lCJGahbOhdCuhV.jpg",
      "release_date": "2024-02-27",
      "title": "Dune: Part Two",
      "video": False,
      "vote_average": 8.2,
      "vote_count": 4324
    },
    {
      "adult": False,
      "backdrop_path": "/1m1rXopfNDVL3UMiv6kriYaJ3yE.jpg",
      "genre_ids": [
        28,
        53,
        80,
        878
      ],
      "id": 882059,
      "original_language": "en",
      "original_title": "Boy Kills World",
      "overview": "When his family is murdered, a deaf-mute named Boy escapes to the jungle and is trained by a mysterious shaman to repress his childish imagination and become an instrument of death.",
      "popularity": 891.24,
      "poster_path": "/25JskXmchcYwj3jHRmcPm738MpB.jpg",
      "release_date": "2024-04-24",
      "title": "Boy Kills World",
      "video": False,
      "vote_average": 6.901,
      "vote_count": 218
    },
    {
      "adult": False,
      "backdrop_path": "/s9hW1DHfgy5ppK1fTUJuMKh4YFK.jpg",
      "genre_ids": [
        28,
        53
      ],
      "id": 980083,
      "original_language": "en",
      "original_title": "Top Gunner: Danger Zone",
      "overview": "An airliner filled with 800 passengers is forced to fly fast and low, above farmlands, suburbs and skyscraper-packed cities or the tons of explosives aboard will detonate. When an elite unit of US Air Force fighter jets is sent to provide escort, they find themselves facing a squadron of unidentifiable warplanes which ignites a deadly air battle that threatens to destroy all life above and below.",
      "popularity": 760.265,
      "poster_path": "/29UCk1nvPzn2XubLk5rKDMlHBRu.jpg",
      "release_date": "2022-05-20",
      "title": "Top Gunner: Danger Zone",
      "video": False,
      "vote_average": 4,
      "vote_count": 13
    },
    {
      "adult": False,
      "backdrop_path": "/kYgQzzjNis5jJalYtIHgrom0gOx.jpg",
      "genre_ids": [
        16,
        28,
        10751,
        35,
        14
      ],
      "id": 1011985,
      "original_language": "en",
      "original_title": "Kung Fu Panda 4",
      "overview": "Po is gearing up to become the spiritual leader of his Valley of Peace, but also needs someone to take his place as Dragon Warrior. As such, he will train a new kung fu practitioner for the spot and will encounter a villain called the Chameleon who conjures villains from the past.",
      "popularity": 759.173,
      "poster_path": "/kDp1vUBnMpe8ak4rjgl3cLELqjU.jpg",
      "release_date": "2024-03-02",
      "title": "Kung Fu Panda 4",
      "video": False,
      "vote_average": 7.119,
      "vote_count": 1879
    },
    {
      "adult": False,
      "backdrop_path": "/qjoX7hl721FOiyeHsDkeQ6rFVLl.jpg",
      "genre_ids": [
        16,
        10751,
        18,
        12,
        35
      ],
      "id": 1022789,
      "original_language": "en",
      "original_title": "Inside Out 2",
      "overview": "Teenager Riley's mind headquarters is undergoing a sudden demolition to make room for something entirely unexpected: new Emotions! Joy, Sadness, Anger, Fear and Disgust, who’ve long been running a successful operation by all accounts, aren’t sure how to feel when Anxiety shows up. And it looks like she’s not alone.",
      "popularity": 748.373,
      "poster_path": "/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg",
      "release_date": "2024-06-12",
      "title": "Inside Out 2",
      "video": False,
      "vote_average": 0,
      "vote_count": 0
    },
    {
      "adult": False,
      "backdrop_path": "/iafs5DG5fGq7ef0acl3xlX4BFrs.jpg",
      "genre_ids": [
        18,
        10770
      ],
      "id": 1219685,
      "original_language": "fr",
      "original_title": "Un père idéal",
      "overview": "",
      "popularity": 685.195,
      "poster_path": "/4xJd3uwtL1vCuZgEfEc8JXI9Uyx.jpg",
      "release_date": "2024-04-21",
      "title": "Un père idéal",
      "video": False,
      "vote_average": 5.695,
      "vote_count": 41
    },
    {
      "adult": False,
      "backdrop_path": "/4XM8DUTQb3lhLemJC51Jx4a2EuA.jpg",
      "genre_ids": [
        28,
        80,
        53
      ],
      "id": 385687,
      "original_language": "en",
      "original_title": "Fast X",
      "overview": "Over many missions and against impossible odds, Dom Toretto and his family have outsmarted, out-nerved and outdriven every foe in their path. Now, they confront the most lethal opponent they've ever faced: A terrifying threat emerging from the shadows of the past who's fueled by blood revenge, and who is determined to shatter this family and destroy everything—and everyone—that Dom loves, forever.",
      "popularity": 641.421,
      "poster_path": "/fiVW06jE7z9YnO4trhaMEdclSiC.jpg",
      "release_date": "2023-05-17",
      "title": "Fast X",
      "video": False,
      "vote_average": 7.12,
      "vote_count": 5230
    },
    {
      "adult": False,
      "backdrop_path": "/nb3xI8XI3w4pMVZ38VijbsyBqP4.jpg",
      "genre_ids": [
        18,
        36
      ],
      "id": 872585,
      "original_language": "en",
      "original_title": "Oppenheimer",
      "overview": "The story of J. Robert Oppenheimer's role in the development of the atomic bomb during World War II.",
      "popularity": 625.191,
      "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
      "release_date": "2023-07-19",
      "title": "Oppenheimer",
      "video": False,
      "vote_average": 8.097,
      "vote_count": 8234
    },
    {
      "adult": False,
      "backdrop_path": "/qwK9soQmmJ7kRdjLZVXblw3g7AQ.jpg",
      "genre_ids": [
        28,
        12,
        53,
        80
      ],
      "id": 7451,
      "original_language": "en",
      "original_title": "xXx",
      "overview": "Xander Cage is your standard adrenaline junkie with no fear and a lousy attitude. When the US Government \"recruits\" him to go on a mission, he's not exactly thrilled. His mission: to gather information on an organization that may just be planning the destruction of the world, led by the nihilistic Yorgi.",
      "popularity": 608.16,
      "poster_path": "/xeEw3eLeSFmJgXZzmF2Efww0q3s.jpg",
      "release_date": "2002-08-09",
      "title": "xXx",
      "video": False,
      "vote_average": 5.934,
      "vote_count": 4080
    },
    {
      "adult": False,
      "backdrop_path": "/vWzJDjLPmycnQ42IppEjMpIhrhc.jpg",
      "genre_ids": [
        16,
        35,
        10751,
        12
      ],
      "id": 748783,
      "original_language": "en",
      "original_title": "The Garfield Movie",
      "overview": "Garfield, the world-famous, Monday-hating, lasagna-loving indoor cat, is about to have a wild outdoor adventure! After an unexpected reunion with his long-lost father – scruffy street cat Vic – Garfield and his canine friend Odie are forced from their perfectly pampered life into joining Vic in a hilarious, high-stakes heist.",
      "popularity": 590.776,
      "poster_path": "/p6AbOJvMQhBmffd0PIv0u8ghWeY.jpg",
      "release_date": "2024-04-30",
      "title": "The Garfield Movie",
      "video": False,
      "vote_average": 6.5,
      "vote_count": 136
    },
    {
      "adult": False,
      "backdrop_path": "/tRS6jvPM9qPrrnx2KRp3ew96Yot.jpg",
      "genre_ids": [
        80,
        9648,
        53
      ],
      "id": 414906,
      "original_language": "en",
      "original_title": "The Batman",
      "overview": "In his second year of fighting crime, Batman uncovers corruption in Gotham City that connects to his own family while facing a serial killer known as the Riddler.",
      "popularity": 587.006,
      "poster_path": "/74xTEgt7R36Fpooo50r9T25onhq.jpg",
      "release_date": "2022-03-01",
      "title": "The Batman",
      "video": False,
      "vote_average": 7.676,
      "vote_count": 9673
    }
  ] 

results2=[
    {
      "adult": False,
      "backdrop_path": "/5Eip60UDiPLASyKjmHPMruggTc4.jpg",
      "genre_ids": [
        27,
        9648,
        53
      ],
      "id": 1041613,
      "original_language": "en",
      "original_title": "Immaculate",
      "overview": "An American nun embarks on a new journey when she joins a remote convent in the Italian countryside. However, her warm welcome quickly turns into a living nightmare when she discovers her new home harbours a sinister secret and unspeakable horrors.",
      "popularity": 554.738,
      "poster_path": "/fdZpvODTX5wwkD0ikZNaClE4AoW.jpg",
      "release_date": "2024-03-20",
      "title": "Immaculate",
      "video": False,
      "vote_average": 6.279,
      "vote_count": 552
    },
    {
      "adult": False,
      "backdrop_path": "/wh4ze6klUbeichAj603OKZwY1W5.jpg",
      "genre_ids": [
        28,
        53,
        878
      ],
      "id": 218,
      "original_language": "en",
      "original_title": "The Terminator",
      "overview": "In the post-apocalyptic future, reigning tyrannical supercomputers teleport a cyborg assassin known as the \"Terminator\" back to 1984 to kill Sarah Connor, whose unborn son is destined to lead insurgents against 21st century mechanical hegemony. Meanwhile, the human-resistance movement dispatches a lone warrior to safeguard Sarah. Can he stop the virtually indestructible killing machine?",
      "popularity": 544.967,
      "poster_path": "/qvktm0BHcnmDpul4Hz01GIazWPr.jpg",
      "release_date": "1984-10-26",
      "title": "The Terminator",
      "video": False,
      "vote_average": 7.667,
      "vote_count": 12607
    },
    {
      "adult": False,
      "backdrop_path": "/lzWHmYdfeFiMIY4JaMmtR7GEli3.jpg",
      "genre_ids": [
        878,
        12
      ],
      "id": 438631,
      "original_language": "en",
      "original_title": "Dune",
      "overview": "Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive.",
      "popularity": 540.881,
      "poster_path": "/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
      "release_date": "2021-09-15",
      "title": "Dune",
      "video": False,
      "vote_average": 7.783,
      "vote_count": 11832
    },
    {
      "adult": False,
      "backdrop_path": "/2JmEZtZsGVYvcUeMWze9qb1Ui03.jpg",
      "genre_ids": [
        80,
        28,
        53
      ],
      "id": 573435,
      "original_language": "en",
      "original_title": "Bad Boys: Ride or Die",
      "overview": "After their late former Captain is framed, Lowrey and Burnett try to clear his name, only to end up on the run themselves.",
      "popularity": 532.584,
      "poster_path": "/nP6RliHjxsz4irTKsxe8FRhKZYl.jpg",
      "release_date": "2024-06-05",
      "title": "Bad Boys: Ride or Die",
      "video": False,
      "vote_average": 6.786,
      "vote_count": 14
    },
    {
      "adult": False,
      "backdrop_path": "/42rp8MkwOEFA62wwgKcuOpP8Fjb.jpg",
      "genre_ids": [
        28,
        36,
        18,
        10752
      ],
      "id": 660360,
      "original_language": "ko",
      "original_title": "노량: 죽음의 바다",
      "overview": "In the winter of 1598, the seven-year Imjin War nears an end as the Japanese Wae invaders prepare to withdraw from Joseon. Admiral Yi Sun-shin leads an allied fleet of Joseon and Ming ships to annihilate the Wae army. Joseon, Ming, and Wae forces clash at Noryang Strait, the deadly sea where Admiral Yi fights his last valiant battle.",
      "popularity": 528.237,
      "poster_path": "/wFAe7gA513Pi2meI4ECwf6YEKR1.jpg",
      "release_date": "2023-12-20",
      "title": "Noryang: Deadly Sea",
      "video": False,
      "vote_average": 6.41,
      "vote_count": 78
    },
    {
      "adult": False,
      "backdrop_path": "/yY76zq9XSuJ4nWyPDuwkdV7Wt0c.jpg",
      "genre_ids": [
        28,
        53,
        878
      ],
      "id": 577922,
      "original_language": "en",
      "original_title": "Tenet",
      "overview": "Armed with only one word - Tenet - and fighting for the survival of the entire world, the Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.",
      "popularity": 524.702,
      "poster_path": "/k68nPLbIST6NP96JmTxmZijEvCA.jpg",
      "release_date": "2020-08-22",
      "title": "Tenet",
      "video": False,
      "vote_average": 7.184,
      "vote_count": 9450
    },
    {
      "adult": False,
      "backdrop_path": "/pDKFL1zcHzEpmz4MJA5JJnRbJeD.jpg",
      "genre_ids": [
        27,
        53,
        18
      ],
      "id": 405774,
      "original_language": "en",
      "original_title": "Bird Box",
      "overview": "Five years after an ominous unseen presence drives most of society to suicide, a survivor and her two children make a desperate bid to reach safety.",
      "popularity": 523.967,
      "poster_path": "/rGfGfgL2pEPCfhIvqHXieXFn7gp.jpg",
      "release_date": "2018-12-13",
      "title": "Bird Box",
      "video": False,
      "vote_average": 6.842,
      "vote_count": 9629
    },
    {
      "adult": False,
      "backdrop_path": "/3RWsSQlqzRjsuqSRmoyggy74UA7.jpg",
      "genre_ids": [
        28,
        14,
        35
      ],
      "id": 43074,
      "original_language": "en",
      "original_title": "Ghostbusters",
      "overview": "Following a ghost invasion of Manhattan, paranormal enthusiasts Erin Gilbert and Abby Yates, nuclear engineer Jillian Holtzmann, and subway worker Patty Tolan band together to stop the otherworldly threat.",
      "popularity": 523.192,
      "poster_path": "/wJmWliwXIgZOCCVOcGRBhce7xPS.jpg",
      "release_date": "2016-07-14",
      "title": "Ghostbusters",
      "video": False,
      "vote_average": 5.359,
      "vote_count": 6248
    },
    {
      "adult": False,
      "backdrop_path": "/kaIfm5ryEOwYg8mLbq8HkPuM1Fo.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 284053,
      "original_language": "en",
      "original_title": "Thor: Ragnarok",
      "overview": "Thor is imprisoned on the other side of the universe and finds himself in a race against time to get back to Asgard to stop Ragnarok, the destruction of his home-world and the end of Asgardian civilization, at the hands of a powerful new threat, the ruthless Hela.",
      "popularity": 521.087,
      "poster_path": "/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg",
      "release_date": "2017-10-02",
      "title": "Thor: Ragnarok",
      "video": False,
      "vote_average": 7.593,
      "vote_count": 20264
    },
    {
      "adult": False,
      "backdrop_path": "/ctMserH8g2SeOAnCw5gFjdQF8mo.jpg",
      "genre_ids": [
        35,
        12
      ],
      "id": 346698,
      "original_language": "en",
      "original_title": "Barbie",
      "overview": "Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.",
      "popularity": 517.615,
      "poster_path": "/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg",
      "release_date": "2023-07-19",
      "title": "Barbie",
      "video": False,
      "vote_average": 7.054,
      "vote_count": 8390
    },
    {
      "adult": False,
      "backdrop_path": "/qAzYK4YPSWDc7aa4R43LcwRIAyb.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 299537,
      "original_language": "en",
      "original_title": "Captain Marvel",
      "overview": "The story follows Carol Danvers as she becomes one of the universe’s most powerful heroes when Earth is caught in the middle of a galactic war between two alien races. Set in the 1990s, Captain Marvel is an all-new adventure from a previously unseen period in the history of the Marvel Cinematic Universe.",
      "popularity": 504.682,
      "poster_path": "/AtsgWhDnHTq68L0lLsUrCnM7TjG.jpg",
      "release_date": "2019-03-06",
      "title": "Captain Marvel",
      "video": False,
      "vote_average": 6.821,
      "vote_count": 15317
    },
    {
      "adult": False,
      "backdrop_path": "/yF1eOkaYvwiORauRCPWznV9xVvi.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 298618,
      "original_language": "en",
      "original_title": "The Flash",
      "overview": "When his attempt to save his family inadvertently alters the future, Barry Allen becomes trapped in a reality in which General Zod has returned and there are no Super Heroes to turn to. In order to save the world that he is in and return to the future that he knows, Barry's only hope is to race for his life. But will making the ultimate sacrifice be enough to reset the universe?",
      "popularity": 502.539,
      "poster_path": "/rktDFPbfHfUbArZ6OOOKsXcv0Bm.jpg",
      "release_date": "2023-06-13",
      "title": "The Flash",
      "video": False,
      "vote_average": 6.733,
      "vote_count": 3936
    },
    {
      "adult": False,
      "backdrop_path": "/6iUNJZymJBMXXriQyFZfLAKnjO6.jpg",
      "genre_ids": [
        28,
        12,
        14
      ],
      "id": 297762,
      "original_language": "en",
      "original_title": "Wonder Woman",
      "overview": "An Amazon princess comes to the world of Man in the grips of the First World War to confront the forces of evil and bring an end to human conflict.",
      "popularity": 498.511,
      "poster_path": "/imekS7f1OuHyUP2LAiTEM0zBzUz.jpg",
      "release_date": "2017-05-30",
      "title": "Wonder Woman",
      "video": False,
      "vote_average": 7.228,
      "vote_count": 19566
    },
    {
      "adult": False,
      "backdrop_path": "/VuukZLgaCrho2Ar8Scl9HtV3yD.jpg",
      "genre_ids": [
        878,
        28
      ],
      "id": 335983,
      "original_language": "en",
      "original_title": "Venom",
      "overview": "Investigative journalist Eddie Brock attempts a comeback following a scandal, but accidentally becomes the host of Venom, a violent, super powerful alien symbiote. Soon, he must rely on his newfound powers to protect the world from a shadowy organization looking for a symbiote of their own.",
      "popularity": 489.201,
      "poster_path": "/2uNW4WbgBXL25BAbXGLnLqX71Sw.jpg",
      "release_date": "2018-09-28",
      "title": "Venom",
      "video": False,
      "vote_average": 6.827,
      "vote_count": 15376
    },
    {
      "adult": False,
      "backdrop_path": "/AmR3JG1VQVxU8TfAvljUhfSFUOx.jpg",
      "genre_ids": [
        27,
        878
      ],
      "id": 348,
      "original_language": "en",
      "original_title": "Alien",
      "overview": "During its return to the earth, commercial spaceship Nostromo intercepts a distress signal from a distant planet. When a three-member team of the crew discovers a chamber containing thousands of eggs on the planet, a creature inside one of the eggs attacks an explorer. The entire crew is unaware of the impending nightmare set to descend upon them when the alien parasite planted inside its unfortunate host is birthed.",
      "popularity": 485.236,
      "poster_path": "/vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg",
      "release_date": "1979-05-25",
      "title": "Alien",
      "video": False,
      "vote_average": 8.154,
      "vote_count": 14023
    },
    {
      "adult": False,
      "backdrop_path": "/icmmSD4vTTDKOq2vvdulafOGw93.jpg",
      "genre_ids": [
        28,
        878
      ],
      "id": 603,
      "original_language": "en",
      "original_title": "The Matrix",
      "overview": "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
      "popularity": 484.335,
      "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
      "release_date": "1999-03-31",
      "title": "The Matrix",
      "video": False,
      "vote_average": 8.217,
      "vote_count": 24979
    },
    {
      "adult": False,
      "backdrop_path": "/9X7YweCJw3q8Mcf6GadxReFEksM.jpg",
      "genre_ids": [
        28,
        18,
        878
      ],
      "id": 263115,
      "original_language": "en",
      "original_title": "Logan",
      "overview": "In the near future, a weary Logan cares for an ailing Professor X in a hideout on the Mexican border. But Logan's attempts to hide from the world and his legacy are upended when a young mutant arrives, pursued by dark forces.",
      "popularity": 483.552,
      "poster_path": "/fnbjcRDYn6YviCcePDnGdyAkYsB.jpg",
      "release_date": "2017-02-28",
      "title": "Logan",
      "video": False,
      "vote_average": 7.818,
      "vote_count": 18762
    },
    {
      "adult": False,
      "backdrop_path": "/70Rm9ItxKuEKN8iu6rNjfwAYUCJ.jpg",
      "genre_ids": [
        27,
        53,
        9648
      ],
      "id": 760104,
      "original_language": "en",
      "original_title": "X",
      "overview": "In 1979, a group of young filmmakers set out to make an adult film in rural Texas, but when their reclusive, elderly hosts catch them in the act, the cast find themselves fighting for their lives.",
      "popularity": 481.533,
      "poster_path": "/A7YPhQKdcr6XB1kCUdS4tHifYWd.jpg",
      "release_date": "2022-03-17",
      "title": "X",
      "video": False,
      "vote_average": 6.731,
      "vote_count": 2812
    },
    {
      "adult": False,
      "backdrop_path": "/kK9v1wclQxug6ZUJucD4DTaHgVF.jpg",
      "genre_ids": [
        18
      ],
      "id": 1366,
      "original_language": "en",
      "original_title": "Rocky",
      "overview": "An uneducated collector for a Philadelphia loan shark is given a once-in-a-lifetime opportunity to fight against the world heavyweight boxing champion.",
      "popularity": 473.113,
      "poster_path": "/cqxg1CihGR5ge0i1wYXr4Rdeppu.jpg",
      "release_date": "1976-11-20",
      "title": "Rocky",
      "video": False,
      "vote_average": 7.788,
      "vote_count": 7578
    },
    {
      "adult": False,
      "backdrop_path": "/w5IDXtifKntw0ajv2co7jFlTQDM.jpg",
      "genre_ids": [
        878,
        9648,
        12
      ],
      "id": 62,
      "original_language": "en",
      "original_title": "2001: A Space Odyssey",
      "overview": "Humanity finds a mysterious object buried beneath the lunar surface and sets off to find its origins with the help of HAL 9000, the world's most advanced super computer.",
      "popularity": 470.732,
      "poster_path": "/ve72VxNqjGM69Uky4WTo2bK6rfq.jpg",
      "release_date": "1968-04-02",
      "title": "2001: A Space Odyssey",
      "video": False,
      "vote_average": 8.078,
      "vote_count": 11137
    }
  ]
result=results1+results2

json_data = json.dumps(result)

with open('data.json', 'w') as json_file:
    json_file.write(json_data)