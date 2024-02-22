Version: pre-alpha (dunno how far I'm taking this yet)

The current ER diagram is not fully complete and needs revision, specifically regarding the CaughtPokemon table and thhe potention re-integration of Stats, EffortValues, and IndividualValues assuming I cannot figure out an easy way to keep them separate.

That said, keeping them as one giant CaughtPokemon table would allow for easier setting of default stat values from Species as it reduces the amount of queries needed. (Either that or I just don't understand how to do it yet. Gimme a break, I'm new to Flask and SQLAlchemy.)
