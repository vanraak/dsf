# Package `dsf`


**Package ‘dsf’**

September 11, 2025

**Title** \`\`Data Science Foudations’’

**Version** 0.0.15

**Description**

The **dsf** package provides a collection of datasets used in the book `Data Science Foundations and Machine Learning with Python`.

**URL** <https://github.com/vanraak/dsf>

**Depends** Python (\>= 3.8) and Pandas (\>2.0)

**License** GPL (\>= 2)

**Repository** Pypi

**Authors** Jeroen van Raak and Reza Mohammadi

**Maintainer** Jeroen van Raak, <j.j.f.vanraak@uva.nl>

**NeedsCompilation** no

**Installation**

    pip install dsf

**Usage**

    import dsf
    df=dsf.load('<dataset>')

Replace <dataset> with the name of the dataset, such as ‘bank’, ‘house’, or ‘churn’.

**Example**

    df=dsf.load('bank') # Load the bank dataset.

**Datasets**

The following datasets are included:

- adult
- advertising
- bank
- caravan
- cereal
- churn
- churncredit
- churntel
- corona
- diamonds
- drug
- house
- houseprice
- insurance
- marketing
- mpg
- redwines
- risk
- whitewines

**Documentation**

The full documentation is available at:
<https://github.com/vanraak/dsf/blob/main/README.pdf>
