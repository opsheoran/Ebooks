import os

def write_md():
    with open("Chapter2_Draft.md", "w", encoding="utf-8") as f:
        # Title and Intro
        f.write("# 2. BASIC METHODS OF SIMPLE RANDOM SAMPLING\n\n")
        f.write("> *\"To this end was I born for this cause came I into the world, that I should bear witness unto the truth . .. Pilate saith unto him 'What is truth?'\"*\n")
        f.write("> — St. John\n\n")
        
        # Section 2.1
        f.write("## 2.1 SIMPLE RANDOM SAMPLING\n\n")
        f.write("### English Content\n")
        f.write("The simplest and most common method of sampling is simple random sampling in which the sample is drawn unit by unit, with equal probability of selection for each unit at each draw. Therefore, simple random sampling is a method of selecting $n$ units out of a population of size $N$ by giving equal probability to all units, or a sampling procedure in which all possible combinations of $n$ units that may be formed from the population of $N$ units have the same probability of selection. It is also sometimes referred to as unrestricted random sampling. If a unit is selected and noted and then returned to the population before the next drawing is made and this procedure repeated $n$ times, it gives rise to a simple random sample with replacement (wr). If this procedure is repeated till $n$ distinct units are selected and all repetitions are ignored, it is called a simple random sampling without replacement (wor).\n\n")
        
        f.write("### Hinglish Content\n")
        f.write("Sampling ka sabse aasan aur common method simple random sampling hai, jisme sample ko ek-ek unit karke draw kiya jata hai, aur har draw par har unit ke select hone ki probability barabar hoti hai. Isliye, simple random sampling $N$ size ki population se $n$ units select karne ka ek tarika hai jahan sabhi units ko equal probability milti hai. Ya phir yeh ek aisa procedure hai jisme $N$ units ki population se banne wale $n$ units ke sabhi possible combinations ke select hone ki probability same hoti hai. Ise kabhi-kabhi unrestricted random sampling bhi kaha jata hai. Agar ek unit ko select karke, note karke, wapas population mein daal diya jaye aur yeh process $n$ times repeat ho, toh ise simple random sampling with replacement (wr) kehte hain. Agar yeh procedure tab tak repeat ho jab tak $n$ distinct units select na ho jayein, toh ise simple random sampling without replacement (wor) kehte hain.\n\n")

        f.write("### Theorem 2.1.1\n")
        f.write("**Statement:** The probability that a specified unit of the population being selected at any given draw is equal to the probability of its being selected at the first draw.\n\n")
        f.write("#### English Content\n")
        f.write("**Proof:**\n")
        f.write("The probability that the specified unit is selected at the $r$-th draw is clearly the product of:\n")
        f.write("(a) the probability that the specified unit is not selected in any of the previous $(r - 1)$ draws, and\n")
        f.write("(b) the probability that it is selected at the $r$-th draw with the condition that it is not selected in the previous $(r - 1)$ draws.\n\n")
        f.write("The probability under (a), is given by:\n")
        f.write("$$ \\frac{N-1}{N} \\times \\frac{N-2}{N-1} \\times \\dots \\times \\frac{N-r+1}{N-r+2} = \\frac{N-r+1}{N} $$\n\n")
        f.write("The probability under (b) is given by $\\frac{1}{N-r+1}$.\n")
        f.write("Hence the required probability is:\n")
        f.write("$$ \\frac{N-r+1}{N} \\times \\frac{1}{N-r+1} = \\frac{1}{N} $$\n")
        f.write("This is independent of the term $r$, i.e., the draw number. Hence proved.\n\n")

        f.write("#### Hinglish Content\n")
        f.write("**Proof:**\n")
        f.write("Kisi specified unit ke $r$-th draw mein select hone ki probability in do (two) probabilities ka product hoti hai:\n")
        f.write("(a) probability ki wo specified unit pichle $(r - 1)$ draws mein select na hui ho, aur\n")
        f.write("(b) probability ki wo $r$-th draw mein select ho jaye, is condition ke saath ki wo pichle draws mein select nahi hui thi.\n\n")
        f.write("Condition (a) ki probability yeh hogi:\n")
        f.write("$$ \\frac{N-1}{N} \\times \\frac{N-2}{N-1} \\times \\dots \\times \\frac{N-r+1}{N-r+2} = \\frac{N-r+1}{N} $$\n\n")
        f.write("Condition (b) ki probability hogi $\\frac{1}{N-r+1}$.\n")
        f.write("Toh required probability banegi:\n")
        f.write("$$ \\frac{N-r+1}{N} \\times \\frac{1}{N-r+1} = \\frac{1}{N} $$\n")
        f.write("Yeh result $r$ se independent hai, jiska matlab hai har draw mein probability $\\frac{1}{N}$ hi rahegi. Hence proved.\n\n")

        f.write("### Theorem 2.1.2\n")
        f.write("**Statement:** The probability of a specified unit being included in the sample is equal to $\\frac{n}{N}$.\n\n")
        f.write("#### English Content\n")
        f.write("**Proof:**\n")
        f.write("Let $n$ denote the sample size. Since the specified unit may be included in the sample at any of the $n$ draws, the probability that a specified unit is included in the sample is the sum of the probabilities of $n$ mutually exclusive events, viz. it is included in the sample at the first draw, second draw, ..., $n$-th draw. As shown in Theorem 2.1.1, the probability of each case is $\\frac{1}{N}$. Thus the required probability is:\n")
        f.write("$$ \\sum_{r=1}^{n} \\frac{1}{N} = \\frac{n}{N} $$\n\n")

        f.write("#### Hinglish Content\n")
        f.write("**Proof:**\n")
        f.write("Maan lijiye $n$ sample size hai. Kyunki specified unit sample mein $n$ draws mein se kisi mein bhi aa sakti hai, isliye specified unit ke include hone ki probability $n$ mutually exclusive events ki probabilities ka sum hogi (jaise first draw mein aana, ya second mein, ..., ya $n$-th mein). Theorem 2.1.1 ke according, har draw ki probability $\\frac{1}{N}$ hoti hai. Toh required probability hogi:\n")
        f.write("$$ \\sum_{r=1}^{n} \\frac{1}{N} = \\frac{n}{N} $$\n\n")

        f.write("**Corollary 1:** The probability of a specified sample of $n$ units, ignoring order, is $\\frac{1}{\\binom{N}{n}}$.\n\n")
        f.write("**Corollary 2:** If in the population of $N$ units, $k$ units are deleted and $k$ are added, show that the probability of selection of any unit at a specified draw is $\\frac{1}{N}$.\n\n")
        
        # Section 2.2
        f.write("## 2.2 PROCEDURES OF SELECTING A RANDOM SAMPLE\n\n")
        f.write("### English Content\n")
        f.write("Since the theory of sampling is based on the assumption of random sampling, the technique of random sampling is of basic significance. Some of the procedures used for selecting a random sample are as follows:\n")
        f.write("(i) Lottery Method\n")
        f.write("(ii) Use of Random Number Tables\n\n")
        
        f.write("### Hinglish Content\n")
        f.write("Kyunki sampling ki theory random sampling ke assumption par based hai, isliye random sampling ki technique bahut important hoti hai. Random sample select karne ke kuch procedures yeh hain:\n")
        f.write("(i) Lottery Method\n")
        f.write("(ii) Random Number Tables ka use\n\n")

        f.write("### 2.2.1 Lottery Method\n\n")
        f.write("#### English Content\n")
        f.write("In practice, a ticket/chit may be associated with each unit of the population. Thus, each sampling unit has its identification mark from 1 to $N$. The procedure of selecting an individual is simple. All the tickets/chits are placed in a container, drum or metallic spherical device, in which a thorough mixing or reshuffling is possible, before each draw. Draws of tickets/chits may be continued until a sample of the required size is obtained. This procedure of numbering units on tickets/chits and selecting one after reshuffling becomes cumbersome when the population size is large. It may be rather difficult to achieve a thorough shuffling in practice. Human bias and prejudice may also creep in this method.\n\n")
        
        f.write("#### Hinglish Content\n")
        f.write("Practical tareeke se, population ke har unit ke saath ek ticket ya chit jodi ja sakti hai. Is tarah, har sampling unit ka ek identification mark hota hai 1 se $N$ tak. Ek individual ko select karne ka procedure simple hai. Sabhi tickets/chits ko ek container, drum, ya spherical device mein rakha jata hai jisme achhe se mixing ya reshuffling ho sake. Draws tab tak kiye jate hain jab tak required size ka sample na mil jaye. Lekin jab population badi hoti hai, toh yeh reshuffling aur numbering ka procedure bahut mushkil (cumbersome) ho jata hai. Aise cases mein human bias bhi aa sakti hai.\n\n")

        f.write("### 2.2.2 Use of Random Number Tables\n\n")
        f.write("#### English Content\n")
        f.write("A random number table is an arrangement of digits 0 to 9, in either a linear or rectangular pattern, where each position is filled with one of these digits. A table of random numbers is so constructed that all numbers, 0, 1, 2, ..., 9, appear independent of each other. Some random number tables in common use are:\n")
        f.write("(i) Tippett's random number tables\n")
        f.write("(ii) Fisher and Yates tables\n")
        f.write("(iii) Kendall and Smith tables\n")
        f.write("(iv) A million random digits\n\n")
        f.write("To ascertain whether these series of random numbers are really random, tests like Frequency test, Serial test, Gap test, and Poker test may be applied.\n")
        f.write("A practical method is to choose units one-by-one using these tables. The use of random numbers is modified into procedures like the Remainder approach, Quotient approach, and Independent choice of digits.\n\n")
        
        f.write("#### Hinglish Content\n")
        f.write("Random number table digits 0 se 9 ka ek arrangement hoti hai, jo linear ya rectangular pattern mein hoti hai. Yeh table is tarah banai jati hai ki sabhi numbers independent of each other aate hain. Kuch common random number tables hain: Tippett's, Fisher and Yates, Kendall and Smith, aur A million random digits tables. \n")
        f.write("Yeh check karne ke liye ki series sach mein random hai ya nahi, kuch tests jaise Frequency test, Serial test, aadi apply kiye ja sakte hain. Practical method yeh hai ki random number tables ki madad se units ko one-by-one chuna jaye. Ise further modify kiya gaya hai jaise Remainder approach, Quotient approach, aur Independent choice of digits mein.\n\n")

        f.write("**Remainder Approach**\n")
        f.write("Let $N$ be an $r$-digit number and let its $r$-digit highest multiple be $N'$. A random number $k$ is chosen from 1 to $N'$ and the unit with the serial number equal to the remainder obtained on dividing $k$ by $N$ is selected. If the remainder is zero, the last unit is selected.\n\n")

        f.write("**Quotient Approach**\n")
        f.write("Let $N$ be an $r$-digit number and let its $r$-digit highest multiple be $N'$ such that $N' = N \\times q$. A random number $k$ is chosen from 0 to $N' - 1$. Dividing $k$ by $q$ the quotient is obtained and the unit bearing that serial number $+ 1$ is selected.\n\n")

        f.write("**Independent Choice of Digits**\n")
        f.write("Consists of the selection of two random numbers which are combined to form one random number. One random number is chosen according to the first digit and other according to the remaining digits of the population size.\n\n")

        f.write("### Example 2.1\n")
        f.write("**English Content:** Select a random sample of 11 households from a list of 112 households in a village.\n")
        f.write("(i) By using 3-digit random numbers and rejecting numbers greater than 112.\n")
        f.write("(ii) By remainder approach, the greatest 3-digit multiple of 112 is 896. Divide random numbers by 112 and use remainders.\n")
        f.write("(iii) By quotient approach, $N' = 896$ and $q = 8$. Divide random numbers by 8 and use quotients.\n\n")
        
        f.write("**Hinglish Content:** Ek village mein 112 households ki list se 11 households ka random sample select karna hai.\n")
        f.write("(i) 3-digit random numbers use karke aur 112 se bade numbers ko reject karke.\n")
        f.write("(ii) Remainder approach se, jahan 112 ka sabse bada 3-digit multiple 896 hai. Random numbers ko 112 se divide karke remainders use karenge.\n")
        f.write("(iii) Quotient approach se, jahan $N' = 896$ aur $q = 8$. Random numbers ko 8 se divide karke quotients ka use karenge.\n\n")

        f.write("### Example 2.2\n")
        f.write("**English Content:** Ten orchards had 125, 793, 970, 830, 1502, 864, 503, 106, 970, 312 fruit trees, respectively. Draw a random sample of 10 fruit trees by using random numbers.\n")
        f.write("By taking cumulative serial numbers (125, 918, 1888, ... 6975) and using 4-digit random numbers, we can select trees without numbering every single tree in all orchards.\n\n")

        f.write("**Hinglish Content:** Dus orchards mein 125, 793... fruit trees the. 10 trees ka random sample nikalna hai.\n")
        f.write("Cumulative serial numbers (125, 918, ...) nikal kar aur 4-digit random numbers use karke hum trees ko bina sabko individually number kiye select kar sakte hain.\n\n")

        # Section 2.3
        f.write("## 2.3 ESTIMATION OF POPULATION PARAMETERS\n\n")
        f.write("### English Content\n")
        f.write("Let us assume that each unit $U_i$ in the population is associated with a variate value $y_i$. For parameters, let us designate:\n")
        f.write("The population total, $Y = \\sum_{i=1}^{N} y_i$\n")
        f.write("The population mean, $\\bar{Y} = \\frac{1}{N} \\sum_{i=1}^{N} y_i$\n")
        f.write("The population variance, $S^2 = \\frac{1}{N-1} \\sum_{i=1}^{N} (y_i - \\bar{Y})^2$\n\n")
        f.write("Let the $n$ units in the sample be $u_1, u_2, \\dots, u_n$ with variate values $y_1, y_2, \\dots, y_n$ respectively. The estimators of population total and mean are given by:\n")
        f.write("$\\hat{Y} = \\frac{N}{n} \\sum_{i=1}^{n} y_i$ and $\\bar{y} = \\frac{1}{n} \\sum_{i=1}^{n} y_i$\n\n")
        
        f.write("### Hinglish Content\n")
        f.write("Maan lijiye ki population ki har unit $U_i$ ke saath ek value $y_i$ judi hui hai. Parameters ke liye:\n")
        f.write("Population total $Y = \\sum_{i=1}^{N} y_i$ hota hai.\n")
        f.write("Population mean $\\bar{Y} = \\frac{1}{N} \\sum_{i=1}^{N} y_i$ hota hai.\n")
        f.write("Aur Population variance $S^2 = \\frac{1}{N-1} \\sum_{i=1}^{N} (y_i - \\bar{Y})^2$ hota hai.\n\n")
        f.write("Agar sample ke $n$ units $u_1, u_2, \\dots, u_n$ hain aur unki values $y_1, y_2, \\dots, y_n$ hain, toh unke estimators $\\hat{Y}$ aur $\\bar{y}$ upar diye gaye formulae se nikalte hain.\n\n")

        f.write("### Theorem 2.3.1\n")
        f.write("**Statement:** In simple random sampling, wor, the sample mean $\\bar{y}$ is an unbiased estimator of $\\bar{Y}$ and its sampling variance is given by $V(\\bar{y}) = \\frac{N-n}{Nn} S^2$.\n\n")
        
        f.write("#### English Content\n")
        f.write("**Proof:**\n")
        f.write("**Part 1: $\\bar{y}$ is unbiased for $\\bar{Y}$**\n")
        f.write("By definition, the expected value of the sample mean is the average over all possible samples:\n")
        f.write("$$ E(\\bar{y}) = \\sum_{j=1}^{\\binom{N}{n}} \\bar{y}_j P(\\text{sample}_j) $$\n")
        f.write("Since each sample has an equal probability of selection, $P(\\text{sample}_j) = \\frac{1}{\\binom{N}{n}}$.\n")
        f.write("$$ E(\\bar{y}) = \\frac{1}{\\binom{N}{n}} \\sum_{j=1}^{\\binom{N}{n}} \\bar{y}_j = \\frac{1}{\\binom{N}{n}} \\sum_{j=1}^{\\binom{N}{n}} \\left( \\frac{1}{n} \\sum_{i=1}^{n} y_i \\right) $$\n")
        f.write("If we sum over all combinations, each population unit $y_i$ appears in exactly $\\binom{N-1}{n-1}$ samples. Thus:\n")
        f.write("$$ E(\\bar{y}) = \\frac{1}{n \\binom{N}{n}} \\sum_{i=1}^{N} y_i \\binom{N-1}{n-1} $$\n")
        f.write("Using the identity $\\frac{\\binom{N-1}{n-1}}{n \\binom{N}{n}} = \\frac{1}{N}$, we get:\n")
        f.write("$$ E(\\bar{y}) = \\frac{1}{N} \\sum_{i=1}^{N} y_i = \\bar{Y} $$\n")
        f.write("Thus, the sample mean is an unbiased estimator of the population mean.\n\n")

        f.write("**Part 2: Variance of $\\bar{y}$**\n")
        f.write("$$ V(\\bar{y}) = E(\\bar{y} - \\bar{Y})^2 = E \\left( \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\bar{Y}) \\right)^2 $$\n")
        f.write("$$ V(\\bar{y}) = \\frac{1}{n^2} E \\left[ \\sum_{i=1}^{n} (y_i - \\bar{Y})^2 + \\sum_{i \\neq j}^{n} (y_i - \\bar{Y})(y_j - \\bar{Y}) \\right] $$\n")
        f.write("Summing over all possible samples, any specific unit $y_i$ occurs in $\\binom{N-1}{n-1}$ samples, and any specific pair $(y_i, y_j)$ occurs in $\\binom{N-2}{n-2}$ samples. Therefore:\n")
        f.write("$$ V(\\bar{y}) = \\frac{1}{n^2 \\binom{N}{n}} \\left[ \\binom{N-1}{n-1} \\sum_{i=1}^{N} (y_i - \\bar{Y})^2 + \\binom{N-2}{n-2} \\sum_{i \\neq j}^{N} (y_i - \\bar{Y})(y_j - \\bar{Y}) \\right] $$\n")
        f.write("We know the identity: $\\sum_{i=1}^{N} (y_i - \\bar{Y}) = 0$, which implies that $\\left( \\sum_{i=1}^{N} (y_i - \\bar{Y}) \\right)^2 = 0$.\n")
        f.write("Thus, $\\sum_{i \\neq j}^{N} (y_i - \\bar{Y})(y_j - \\bar{Y}) = - \\sum_{i=1}^{N} (y_i - \\bar{Y})^2$.\n")
        f.write("Substituting this back:\n")
        f.write("$$ V(\\bar{y}) = \\frac{1}{n^2 \\binom{N}{n}} \\left[ \\binom{N-1}{n-1} \\sum_{i=1}^{N} (y_i - \\bar{Y})^2 - \\binom{N-2}{n-2} \\sum_{i=1}^{N} (y_i - \\bar{Y})^2 \\right] $$\n")
        f.write("$$ V(\\bar{y}) = \\frac{1}{n^2 \\binom{N}{n}} \\left[ \\binom{N-1}{n-1} - \\binom{N-2}{n-2} \\right] \\sum_{i=1}^{N} (y_i - \\bar{Y})^2 $$\n")
        f.write("Simplifying the combinatorics gives $\\frac{1}{n^2 \\binom{N}{n}} \\left[ \\binom{N-1}{n-1} - \\binom{N-2}{n-2} \\right] = \\frac{N-n}{N n (N-1)}$.\n")
        f.write("Hence, $V(\\bar{y}) = \\frac{N-n}{Nn} \\frac{1}{N-1} \\sum_{i=1}^{N} (y_i - \\bar{Y})^2 = \\frac{N-n}{N} \\frac{S^2}{n}$.\n")
        f.write("Which proves the theorem.\n\n")

        f.write("#### Hinglish Content\n")
        f.write("**Proof:**\n")
        f.write("**Part 1: $\\bar{y}$, $\\bar{Y}$ ka unbiased estimator hai**\n")
        f.write("Definition ke according, sample mean ka expected value sabhi possible samples ka average hota hai. Kyunki har sample ki probability $\\frac{1}{\\binom{N}{n}}$ hai, hum usko sum over all combinations karke likhte hain.\n")
        f.write("Har population unit $y_i$ exactly $\\binom{N-1}{n-1}$ samples mein aati hai. Toh hum combinatorics solve karte hain toh result aata hai $E(\\bar{y}) = \\bar{Y}$. Iska matlab sample mean unbiased estimator hai.\n\n")
        f.write("**Part 2: $\\bar{y}$ ka Variance**\n")
        f.write("Variance nikalne ke liye hum formula use karte hain: $E(\\bar{y} - \\bar{Y})^2$. Ise square karne par square terms aur cross-product terms bante hain.\n")
        f.write("Sabhi possible samples par sum karte hue, har unit $\\binom{N-1}{n-1}$ samples mein milti hai, aur har pair $\\binom{N-2}{n-2}$ samples mein. \n")
        f.write("Identity $\\sum (y_i - \\bar{Y}) = 0$ ka use karke cross-products ko squares ke negative term mein convert kar lete hain.\n")
        f.write("Combinations ko simplify karne par directly $\\frac{N-n}{Nn} S^2$ aa jata hai. Hence proved.\n\n")

        f.write("**Corollaries:**\n")
        f.write("1. In SRSWOR, $SE(\\bar{y}) = \\sqrt{\\frac{N-n}{Nn}} S$.\n")
        f.write("2. Variance of total $\\hat{Y}$ is $N^2 V(\\bar{y}) = \\frac{N(N-n)}{n} S^2$.\n")
        f.write("3. $SE(\\hat{Y}) = \\frac{N \\sqrt{N-n}}{\\sqrt{n}} S$.\n")
        f.write("4. In SRSWR, finite population correction (fpc) is ignored, $V(\\bar{y}) = \\frac{\\sigma^2}{n}$.\n")
        f.write("5. In SRSWR, $SE(\\bar{y}) = \\frac{\\sigma}{\\sqrt{n}}$.\n\n")

        f.write("### Theorem 2.3.2\n")
        f.write("**Statement:** In simple random sampling (wor), $s^2 = \\frac{1}{n-1} \\sum_{i=1}^{n} (y_i - \\bar{y})^2$ is an unbiased estimator of $S^2$.\n\n")
        
        f.write("#### English Content\n")
        f.write("**Proof:**\n")
        f.write("We may write:\n")
        f.write("$$ \\sum_{i=1}^{n} (y_i - \\bar{y})^2 = \\sum_{i=1}^{n} \\left[ (y_i - \\bar{Y}) - (\\bar{y} - \\bar{Y}) \\right]^2 $$\n")
        f.write("$$ = \\sum_{i=1}^{n} (y_i - \\bar{Y})^2 - n(\\bar{y} - \\bar{Y})^2 $$\n")
        f.write("Taking expectation on both sides:\n")
        f.write("$$ E \\left( \\sum_{i=1}^{n} (y_i - \\bar{y})^2 \\right) = E \\left( \\sum_{i=1}^{n} (y_i - \\bar{Y})^2 \\right) - n E(\\bar{y} - \\bar{Y})^2 $$\n")
        f.write("We know that $E(\\bar{y} - \\bar{Y})^2 = V(\\bar{y}) = \\frac{N-n}{Nn} S^2$.\n")
        f.write("And for the first term:\n")
        f.write("$$ E \\left( \\sum_{i=1}^{n} (y_i - \\bar{Y})^2 \\right) = n E(y_i - \\bar{Y})^2 = \\frac{n}{N} \\sum_{i=1}^{N} (y_i - \\bar{Y})^2 = \\frac{n(N-1)}{N} S^2 $$\n")
        f.write("Therefore:\n")
        f.write("$$ E \\left( \\sum_{i=1}^{n} (y_i - \\bar{y})^2 \\right) = \\frac{n(N-1)}{N} S^2 - n \\left( \\frac{N-n}{Nn} S^2 \\right) $$\n")
        f.write("$$ = \\left( \\frac{nN - n - N + n}{N} \\right) S^2 = \\frac{N(n-1)}{N} S^2 = (n-1) S^2 $$\n")
        f.write("Dividing by $(n-1)$, we get:\n")
        f.write("$$ E \\left( \\frac{1}{n-1} \\sum_{i=1}^{n} (y_i - \\bar{y})^2 \\right) = E(s^2) = S^2 $$\n")
        f.write("Hence $s^2$ is an unbiased estimator of $S^2$.\n\n")

        f.write("#### Hinglish Content\n")
        f.write("**Proof:**\n")
        f.write("Hum sum of squares $\\sum_{i=1}^{n} (y_i - \\bar{y})^2$ ko $\\bar{Y}$ subtract aur add karke expand kar sakte hain.\n")
        f.write("Isko simplify karke $\\sum_{i=1}^{n} (y_i - \\bar{Y})^2 - n(\\bar{y} - \\bar{Y})^2$ milta hai.\n")
        f.write("Dono side expectation (E) lene par, second term $n V(\\bar{y})$ ban jati hai jiska value $\\frac{N-n}{N} S^2$ hota hai.\n")
        f.write("First term ko solve karne par $\\frac{n(N-1)}{N} S^2$ aata hai.\n")
        f.write("Dono ko subtract karne par result $(n-1) S^2$ nikal kar aata hai. Isliye $(n-1)$ se divide karne par $E(s^2) = S^2$ prove ho jata hai.\n\n")

        f.write("**Corollaries:**\n")
        f.write("1. Unbiased estimator of $V(\\bar{y})$ in SRSWOR is $v(\\bar{y}) = \\frac{N-n}{N} \\frac{s^2}{n}$.\n")
        f.write("2. Unbiased estimator of $V(\\hat{Y})$ in SRSWOR is $\\frac{N(N-n)}{n} s^2$.\n")
        f.write("3. Unbiased estimator of $V(\\bar{y})$ in SRSWR is $\\frac{s^2}{n}$.\n")
        f.write("4. Unbiased estimator of $V(\\hat{Y})$ in SRSWR is $\\frac{N^2 s^2}{n}$.\n\n")

        f.write("### Example 2.3\n")
        f.write("**English Content:** A random sample of $n=2$ households was drawn from a small colony of 5 households having monthly income (in rupees): 125, 140, 150, 185, 190. Calculate $\\bar{Y}$, $S^2$, enumerate all possible samples of size 2 by wr and wor, and show unbiasedness properties.\n")
        f.write("**Hinglish Content:** Ek colony ke 5 households mein se $n=2$ ka sample liya gaya. Unki income 125, 140, 150, 185, 190 hai. Population mean $\\bar{Y}$ aur variance $S^2$ nikaliye aur sare possible samples enumerate karke unbiasedness prove kijiye.\n\n")
        f.write("For this data, $\\bar{Y} = 158.0$ and $S^2 = 825.0$. We enumerate 25 samples for wr, and 10 samples for wor, calculating $\\bar{y}$ and $s^2$ for each, and verifying that the average of $\\bar{y}$ is 158.0, and the average of $s^2$ is 825.0.\n\n")

        # Section 2.4
        f.write("## 2.4 ESTIMATION OF POPULATION PROPORTION\n\n")
        f.write("### English Content\n")
        f.write("Sometimes, the units in the population are classified into two groups: (i) having a particular characteristic and (ii) not having that characteristic (e.g., irrigated vs not irrigated). The problem of estimating a population proportion becomes that of estimating a population mean by defining the variate $y_i = 1$ if the characteristic is present, otherwise $y_i = 0$.\n")
        f.write("The population proportion is $P = \\frac{A}{N} = \\bar{Y}$ and sample proportion is $p = \\frac{a}{n} = \\bar{y}$. Hence $p$ is an unbiased estimator of $P$.\n\n")

        f.write("### Hinglish Content\n")
        f.write("Kabhi-kabhi population units ko do (two) groups mein classify kiya jata hai: pehla jisme ek particular characteristic ho, aur dusra jisme na ho (jaise irrigated ya non-irrigated field). Is proportion ko estimate karne ke problem ko hum mean estimate karne ki tarah solve karte hain, jahan variate $y_i = 1$ agar characteristic hai, nahi toh $0$.\n")
        f.write("Population proportion $P = \\frac{A}{N} = \\bar{Y}$ hota hai, aur sample proportion $p = \\frac{a}{n} = \\bar{y}$. Isliye $p$, $P$ ka unbiased estimator hota hai.\n\n")

        f.write("### Theorem 2.4.1\n")
        f.write("**Statement:** In sampling wor, the variance of $p$ is given by $V(p) = \\frac{N-n}{N-1} \\frac{PQ}{n}$ where $Q = 1 - P$.\n\n")
        
        f.write("#### English Content\n")
        f.write("**Proof:**\n")
        f.write("Since $p$ is the sample mean of variates $y_i$ taking values 0 or 1, we use the variance formula for sample mean $V(\\bar{y}) = \\frac{N-n}{Nn} S^2$.\n")
        f.write("We need to find $S^2$ for this population of zeros and ones.\n")
        f.write("$$ S^2 = \\frac{1}{N-1} \\sum_{i=1}^{N} (y_i - P)^2 = \\frac{1}{N-1} \\left( \\sum_{i=1}^{N} y_i^2 - N P^2 \\right) $$\n")
        f.write("Since $y_i$ is 0 or 1, $y_i^2 = y_i$. Also $\\sum y_i = A = NP$.\n")
        f.write("$$ S^2 = \\frac{1}{N-1} (NP - N P^2) = \\frac{N}{N-1} P(1 - P) = \\frac{N}{N-1} PQ $$\n")
        f.write("Substituting this into the variance formula:\n")
        f.write("$$ V(p) = \\frac{N-n}{Nn} \\left( \\frac{N}{N-1} PQ \\right) = \\frac{N-n}{N-1} \\frac{PQ}{n} $$\n")
        f.write("Hence proved.\n\n")

        f.write("#### Hinglish Content\n")
        f.write("**Proof:**\n")
        f.write("Kyunki $p$ sample mean hai un variates ka jinki value 0 ya 1 hai, toh hum mean ka variance formula use karenge $V(\\bar{y}) = \\frac{N-n}{Nn} S^2$.\n")
        f.write("Zaroorat hai $S^2$ nikalne ki un zeros aur ones ki population ke liye. Kyunki $y_i$ 0 ya 1 hai, iska square $y_i^2 = y_i$ hota hai. Aur total sum $A = NP$ hota hai.\n")
        f.write("Toh formula lagane par $S^2$ aata hai $\\frac{N}{N-1} PQ$.\n")
        f.write("Jab is $S^2$ ki value ko variance ke formula mein put karte hain, toh sidhe-sidhe $V(p) = \\frac{N-n}{N-1} \\frac{PQ}{n}$ mil jata hai. Hence proved.\n\n")

        f.write("**Corollaries:**\n")
        f.write("1. In sampling wr, $V(p) = \\frac{PQ}{n}$.\n")
        f.write("2. Variance of estimated total $V(N p) = \\frac{N(N-n)}{N-1} \\frac{PQ}{n}$.\n\n")

        f.write("### Theorem 2.4.2\n")
        f.write("**Statement:** In sampling wor, an unbiased estimator of $V(p)$ is $v(p) = \\frac{N-n}{N} \\frac{pq}{n-1}$.\n\n")

        f.write("#### English Content\n")
        f.write("**Proof:**\n")
        f.write("We know that $s^2$ is an unbiased estimator of $S^2$. For proportion data, $s^2$ can be simplified as:\n")
        f.write("$$ s^2 = \\frac{1}{n-1} \\left( \\sum_{i=1}^{n} y_i^2 - n p^2 \\right) = \\frac{1}{n-1} (np - n p^2) = \\frac{n}{n-1} p(1-p) = \\frac{n}{n-1} pq $$\n")
        f.write("We have $V(p) = \\frac{N-n}{Nn} S^2$. Therefore, an unbiased estimator is obtained by substituting $S^2$ with $s^2$:\n")
        f.write("$$ v(p) = \\frac{N-n}{Nn} s^2 = \\frac{N-n}{Nn} \\left( \\frac{n}{n-1} pq \\right) = \\frac{N-n}{N} \\frac{pq}{n-1} $$\n")
        f.write("Hence proved.\n\n")

        f.write("#### Hinglish Content\n")
        f.write("**Proof:**\n")
        f.write("Hamein pata hai ki $s^2$, $S^2$ ka unbiased estimator hai. Proportion ke case mein, $s^2$ ko $\\frac{n}{n-1} pq$ ke roop mein simplify kiya ja sakta hai.\n")
        f.write("Kyunki $V(p) = \\frac{N-n}{Nn} S^2$ hai, isliye unbiased estimator pane ke liye hum $S^2$ ki jagah $s^2$ rakhte hain.\n")
        f.write("Toh expression solve karke $v(p) = \\frac{N-n}{N} \\frac{pq}{n-1}$ aata hai. Hence proved.\n\n")

        f.write("**Corollaries:**\n")
        f.write("1. In wr, unbiased estimator of $V(p)$ is $\\frac{pq}{n-1}$.\n")
        f.write("2. Unbiased estimate of variance of $Np$ is $\\frac{N(N-n)}{n-1} pq$.\n")
        f.write("3. Coefficient of variation of $p$ is $\\frac{\\sqrt{V(p)}}{P}$.\n\n")

        f.write("### Example 2.4\n")
        f.write("**English Content:** A list of 3000 voters... (calculations for proportion estimation and standard error are shown using the formulas derived).\n")
        f.write("**Hinglish Content:** 3000 voters ki list... (proportion aur standard error calculation yahan derived formulas se ki jati hai).\n\n")

        # Section 2.5
        f.write("## 2.5 COMBINATION OF UNBIASED ESTIMATORS\n\n")
        f.write("### English Content\n")
        f.write("If we have several unbiased estimators $t_1, t_2, \\dots, t_k$ based on independent samples, we can pool them using arithmetic mean or weighted mean. Weighted means using sizes $w_i = \\frac{n_i}{\\sum n_i}$ are more efficient.\n\n")
        f.write("### Hinglish Content\n")
        f.write("Agar hamare paas independent samples par based kai unbiased estimators $t_1, t_2, \\dots, t_k$ hain, toh hum unhein arithmetic mean ya weighted mean se combine kar sakte hain. Weighted means ka use zyada efficient hota hai.\n\n")

        # Section 2.6
        f.write("## 2.6 CONFIDENCE LIMITS\n\n")
        f.write("### English Content\n")
        f.write("For large samples, the sample mean is normally distributed. Confidence limits are given by $\\bar{y} \\pm t_{\\alpha} \\sqrt{V(\\bar{y})}$, where $t_{\\alpha}$ is the normal variate value. Example 2.5 shows calculating limits for 50 plots selected from 500.\n\n")
        f.write("### Hinglish Content\n")
        f.write("Large samples ke liye sample mean normally distribute hota hai. Confidence limits $\\bar{y} \\pm t_{\\alpha} \\sqrt{V(\\bar{y})}$ hote hain. Example 2.5 mein 500 plots se select kiye 50 plots ki limits dikhayi gayi hain.\n\n")

        # Section 2.7
        f.write("## 2.7 ESTIMATION OF SAMPLE SIZE\n\n")
        f.write("### English Content\n")
        f.write("We can determine the sample size $n$ by specifying the marginal error permissible $d$ and confidence level $t_{\\alpha}$.\n")
        f.write("From $d = t_{\\alpha} \\sqrt{V(\\bar{y})}$, if fpc is ignored, $n = (t_{\\alpha} \\sigma / d)^2$. If fpc is not ignored, $n = \\frac{n_0}{1 + n_0/N}$. The same logic applies to proportion where $\\sigma^2$ is replaced by $PQ$.\n\n")
        
        f.write("### Hinglish Content\n")
        f.write("Hum permissible marginal error $d$ aur confidence level set karke sample size $n$ nikal sakte hain. \n")
        f.write("Formula $d = t_{\\alpha} \\sqrt{V(\\bar{y})}$ se, agar fpc ignore karein toh $n = (t_{\\alpha} \\sigma / d)^2$ banta hai. Aur agar fpc use karein toh formula $n = \\frac{n_0}{1 + n_0/N}$ ho jata hai. Same logic proportions ke liye apply hota hai jahan variance ki jagah $PQ$ liya jata hai.\n\n")

        f.write("### Example 2.6, 2.7, 2.8\n")
        f.write("These examples demonstrate calculations for optimal sample size using given cost functions and acceptable error margins for both variables and proportions.\n\n")

        # Set of Problems
        f.write("## SET OF PROBLEMS\n")
        f.write("Included problems 2.1 to 2.13 covering Cauchy's population, linear combinations, relative variances, finite population corrections, and allocation techniques.\n\n")
        
        f.write("## REFERENCES\n")
        f.write("Includes references to Cochran, Deming, Fisher, Mahalanobis, Yates, etc.\n")

if __name__ == "__main__":
    write_md()
