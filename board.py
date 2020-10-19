def board(index):
    hangman =  ["""               ----------
               |        |
               |        0
               |
               |
               |
               """,
           """               ----------
               |        |
               |        0
               |        |
               |
               |
               """,
           """               ----------
               |        |
               |        0
               |       \\|
               |
               |
          """,
           """                ----------
                |        |
                |        0
                |       \\|/
                |
                |
          """,
           """                ----------
                |        |
                |        0
                |       \\|/
                |        |
                |

                """,
           """                ----------
                |        |
                |        0
                |       \\|/
                |        |
                |       /
                """,
           """                ----------
                |        |
                |        0
                |       \\|/
                |        |
                |       / \\

                """]

    return hangman[index]
