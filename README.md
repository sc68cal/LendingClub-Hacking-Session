## [Lending Club][lendingclub] data analysis

This is a small project using Python to analyze [data
posted by LendingClub][data].


### Massaging the dataset

* If you download the data from LendingClub, delete the first row because it
interferes with the [DictReader][dict]'s column detection


### Redis Schema 

* Loan hash
	* Loan::<id>
	* Contains all the data about the loan

* User list
	* Users::
	* Contains a list of all the users' screen names.

* User loans set
	* User::<Screen Name>::Loans
	* Contains IDs of loan hashes that belong to user


[lendingclub]: https://www.lendingclub.com/
[data]: https://www.lendingclub.com/info/download-data.action
[dict]: http://docs.python.org/library/csv.html#csv.DictReader
