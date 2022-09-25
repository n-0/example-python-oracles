# csv_oracle

Scenarios based on the csv_oracle need an initital state (`ConventionalOracleState.parameter`), 
an utf8 byte encoded json of the following form
```json
{
    "files": [
        {
            "path":"/path/to/file.csv",
            "t_mapping": "%m/%d/%Y",
            "mapping": {
               "t":0,
               "o":1,
               "h":2,
               "l":3,
               "c":4,
               "v":7
            }
        }
    ]
}
```

The path leads to the csv file, which should look like this

```csv
01/08/2018,19.037,19.037,19.037,19.037,-0.12,-0.63%,0,0
01/05/2018,19.157,19.157,19.157,19.157,0.027,+0.14%,0,0
01/04/2018,19.13,19.13,19.13,19.13,0.014,+0.07%,0,0
01/03/2018,19.116,19.116,19.116,19.116,0.065,+0.34%,0,0
01/02/2018,19.051,19.051,19.051,19.051,0.061,+0.32%,0,0
```

The t_mapping is the python datetime [format](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior),
and mapping maps the properties of a BasicTick to the column index in the csv file. Notice in the upper example that the
csv file contains more columns than properties of a BasicTick, hence the mapping skips columns 5-6, because percentage changes
are not part of BasicTicks. If the oracle is unable to parse a row it just skips it, therefore files that don't contain any
csv formatted data will result in an empty omen_series.

## Usage
The oracle listens on port `10012` and expects a `persistor` service at port `10000`.
You can use the `create_scenario.py` for easier oracle/scenario persistence.
An example in the python REPL


```python
import oracle

oracle.csv_oracle.create_oracle(['parse_csv', 'some_helpful_alias']) # saves the oracle in the persistor with alias/ticker 'parse_csv'
init_state_palim = {
    'files': [
        {
            'path':"/path/to/file/silver_prices.csv",
            't_mapping': "%m/%d/%Y",
            'mapping': {
               't':0,
               'o':1,
               'h':2,
               'l':3,
               'c':4,
               'v':7
            }
        }
    ]
}
oracle.csv_oracle.create_scenario(
    init_state_palim, # the initial state
    ['scenario_silver_price'], # aliases for scenario
    'parse_csv') # the id or alias of the created oracle
)

oracle.csv_oracle.serve() # start the oracle service
```

Now you can activate the scenario with the alias (`scenario_silver_price`) in the director and you have
an omen_series of ticks for the prices, you're watching.
