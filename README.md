# Working with JSONs

The following object gives you subtotals for this month (October):

```json
{
  "count":15,
  "amount":425,
  "num_items":12,
  "gender":
    {
      "F":
        {
          "count":5,
          "amount":225,
          "num_items":7
        },
      "M":
        {
          "count":10,
          "amount":200,
          "num_items":5
        }
    },
  "currency":
    {
      "EUR":
        {
          "count":13,
          "amount":175,
          "num_items":6
        },
      "USD":
        {
          "count":2,
          "amount":250,
          "num_items":6
        }
    }
}
```

We now have a new entry for October :

```json
{
  "gender": "M",
  "amount": 17.0,
  "num_items": 2,
  "currency": "EUR"
}
```

'add_new_entry' is a function that it add this new entry to the monthly subtotals.

# Run
To run unit test suite, install 'nose', eg. using 'pip': 

    pip install -r ./requirements.txt
    
Run tests:

    nosetests -v


# Author
Jose Bermudez

[www.josebermudez.co.uk](http://www.josebermudez.co.uk)

[info@josebermudez.co.uk](mailto: info@josebermudez.co.uk)