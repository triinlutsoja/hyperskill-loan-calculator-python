# hyperskill-loan-calculator-python
This is the loan calculator I came up with on the Introduction to Python trakc in Hyperskill.

Stage 1/4: Beginning. The calculator takes several parameters like a loan principal and interest, calculates the values the user wants to know (for example, monthly payment or overpayment), and outputs them to the user.

Stage 2/4: Dreamworld. Let's make some calculations for 0% loan repayments. Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount. To perform further calculations, you'll also have to ask for the required missing value. Finally, output the results for the user.

Stage 3/4: Annuity payment. First, you should parse the provided parameters to define, which ones are known and which one is missing.
Compute the missing value using the formulas mentioned above. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal. Finally, output the value users wanted to compute. The final version of your program is supposed to work from the command line and parse the following arguments: --payment, --principal, --periods, --interest. Our loan calculator can't calculate the interest, so it must always be provided.

Stage 4/4: Differentiate payment. Your program should be able to parse new command-line arguments. Let's add the --type one, so now the calculator should be run with 4 arguments: --type, --principal, --periods, --interest. The --type argument must always be provided in any run. Also, it is possible that the user will make a mistake in the provided input. The program should not fail, but inform the user, that he has provided "Incorrect parameters". For differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided. Compute the overpayment: the amount of interest paid over the whole term of the loan.
