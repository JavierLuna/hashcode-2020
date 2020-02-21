# hashcode-2020

IlloDoh's solution to the Hashcode 2020 hackathon.

There's a pdf with the problem statement in the root of the directory.

## How to execute

No extra dependencies are needed, vainilla python 3.6+ works fine.

Execute: `python run.py` and wait for a bit.

The solution will use all your cores by default, but if you want to tweak how many cores the program will use (or the overall configuration), please modify `config.py`.

Solutions will be stored in the `solutions` folder.

## Architectural decisions

To get some context for this decisions, please read the problem statement before.

The solution is composed of five elements that work together:
* `Scheduler`: Holds the logic of what to do on every available day. Uses different policies to sort which libraries to signup/scan first.
* `Policy`: Function which returns a score of a library given certain circunstances to imply its preference before others. Used by the scheduler to make decisions.
* `Registry`: Shared registry of books. Will store the books each library has registered and will avoid duplicates.
* `Library`: Collection of books. Has a certain scan capacity and a certain signup delay. 
* `Book`: Dummy object containing the id and the score of the book.

## Thank you notes

Thanks to my best friend, [David](https://github.com/DavidMendozaMartinez), for sticking with me each and every year to participate together on this hackathon. I'm very proud and happy about how well we work together and how much do we enjoy this kind of challenges.

80/519 in Spain, not bad at all man :)
