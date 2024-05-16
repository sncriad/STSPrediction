### Complete Data Spec:

*Full data (before cleaning): https://drive.google.com/drive/u/1/folders/17O7OPPyqmtizORDlokelunva8B26hpOp*
*Sample data (before cleaning): one of 19 CSV files. https://drive.google.com/file/d/1n1jW5U06dh2Yd4zfd96AS_UUXDpEHDt2/view?usp=drive_link
<br />*


- **Type of data that will be used for the representation:**
Floats (rounded to the nearest thousandth) and Integers.

- **Default value:** 
0 (if no data already there, represented in our CSVs by “-”)

- **Range of value:**
For all float values: [-1, 1], 
For integer values (this applies only to number of estimates): [1, 50].

- **Are these values unique?**
The only unique value in our CSV is the value in position A1, which includes the ticker symbol of the company.

- **Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?**
No, we have 19 distinct companies that we have individually downloaded. We know that there are no duplicated companies.

- **Is this a required value?**
Not necessarily. We are more interested in an overall analysis of how exogenous variables affect the stocks of companies at the top of the S&P than we are interested in analyzing individual companies. It would only be required to remove duplicates. 


- **Do you plan to use this attribute/feature in the analysis? If so, how?**
We were not planning to. However, we could use the ticker symbols to identify concretely the outliers within our 19 companies


- **Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?**
No. The companies have released all this information publicly, and ticker symbols are widely known.

