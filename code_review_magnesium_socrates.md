### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: Magnesium						Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name: 16 / Miguel Angelo F. Socrates		Date: 08/26/2026**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

Implementation 2 is faster, since it runs logarithmically, meaning it can check the list in a few loops, instead of running through the whole code like in implementation one. In the worst case scenario, the list has more than a million values, making implementation 1’s for-loop structure inefficient. On the other hand, Implementation 2 uses terms like low, middle, and high in order to keep the code efficient and fast. Although implementation 2 requires a sorted ascending list of values, it works very efficiently with a large list.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? | How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

At first glance, implementation 1 is easier to understand, since it uses a for loop in order to iterate through the list, instead of a long process like in implementation 2\. The code is compact and concise, since it only uses one for loop inside a function to do its work, making it simple and effective. It is also easy to understand, since variable names are well defined, and return blocks are well placed.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? | How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? |

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

Algorithm 1 would be easier since the code is short and only consists of 5 lines of code that is easy to understand. When you update Algorithm 1 it also has a lower risk of bugs, unlike Algorithm 2 where such a small mistake can lead to an infinite loop. It also operates as its own and doesn't need the numbers to be sorted.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? | Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?

Algorithm 1 would be easier to test because regardless if the number list is short or long you don’t have to sort it according to increasing or decreasing value unlike Algorithm 2\. It also only tests if the number is present or missing in the code. In Algorithm 2 your number list must be sorted or else the code will enter an infinite loop and fail even though the code is correct.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? | Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? |

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from a user?

Both algorithms check if the list is empty and returns \-1 to prevent an infinite loop from happening. Both can handle invalid inputs as long as they’re the same type, if the inputs are mixed with integers and strings, python will issue a “TypeError” on both algorithms. Both algorithms will raise an error to both because they can't handle unusual inputs. Neither algorithm checks the list to ensure that the number is actually in the list. Algorithm 2 will display an incorrect value because it assumes the number list is sorted in ascending order.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search? | Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search? |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

Algorithm 1 would be more suitable for us because it is faster because it only uses a simple for loop to iterate through the number list, making it efficient and easy to change and debug. The conditions that it works best under is when the list is small and easy to process, so that the amount of loops run by the code is minimized, making the algorithm faster. Algorithm 2 would be more suitable for large sorted lists because if your number list is rarely updated Algorithm 2 would pay off over time. All in all, Algorithm 1 is easier to understand and update, and is more suitable for smaller lists and doesn’t require much maintenance compared to Algorithm 2\.