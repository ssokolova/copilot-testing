# Automating Testing with GitHub Copilot
## Revision 1.2 - 06/29/24

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**NOTE: To copy and paste in the codespace, you may need to use keyboard commands - CTRL-C and CTRL-V.**

**Lab 1 - High level Copilot Testing Advice**

**Purpose: In this lab, we’ll start to learn about testing with Copilot at a high levele**

1. In our repository, there is an example Python file we'll be using to start with. You can open it by clicking on [**webscraper.py**](./webscaper.py) , or, in the terminal, enter

```
code webscraper.py
```
 
2. Let's ask Copilot for some general testing advice for this code. Switch to the separate chat area, and ask it:
```
How can I test #file:webscraper.py?
```

3. Copilot will likely have generated some output with a set of instruction and some example code similar to what's shown below. Notice that it brings in unit testing and mocking frameworks.
![testing suggestions for file](./images/ct45.png?raw=true "testing suggestions for file")

4. Let's take the generated code and put it into a new file. Howver over the code section, and click on the 3 dots at the end of the popup bar.
![hover](./images/ct46.png?raw=true "hover")

5. From the menu that pops up, select the *Insert into New File* option and insert the code into a new file in the project.
![insert into new file](./images/ct47.png?raw=true "insert into new file")

6. Now, select the file, and save it. You can use the 3 bar menu on the left, then File->Save and save it as "test_webscraper.py".
![saving as new file](./images/ct47.png?raw=true "saving as new file")

7. Let's also look at how we can add code coverage information for the file. Select the *webscraper.py* file in the editor. Then, we'll just use the shortcut CMD/CTRL+I to bring up the chat dialog and type our question in there.
```
How can I measure code coverage on this file?
```
![query on code coverage](./images/ct48.png?raw=true "query on code coverage")

8. Hit *Enter* and you should see some suggested changes that you can Accept or Reject. You can just go ahead and Accept them for this case.
![query on code coverage](./images/ct49.png?raw=true "query on code coverage")

9. Save any changes to your files.

**Lab 2 - Using other Copilot features to help with testing**

**Purpose: In this lab, we'll see how to leverage some of Copilot's other features to help with testing**

1. First, let's try out the Copilot */tests* shortcut command.  Let's also try it with a different kind of file and language. There's a large demo file of SQL statements in this project named *create-tables.sql*. Open that.
```
code create-tables.sql
```

2. Since this is a different type of file, we will specify the filename when we ask Copilot to generate tests this time. Enter the following question in the chat interface. (It will automatically add an *@workspace* participant at the start, but that's ok.)
```
/tests #file:create-tables.sql?
```
![using /tests command](./images/ct50.png?raw=true "using /tests command")

3. Copilot should respond with some overall instructions/plan and suggested examples of how to do the steps. You can just review these to see the example, you don't need to do anything with them.
![testing suggestions for SQL](./images/ct06.png?raw=true "testing suggestions for sql")   

4. Suppose we need to better understand the code we're testing. We can have Copilot explain the code to us. Highlight all of the code in the file *webscraper.py* and then use the CMD/CTRL+I shortcut to bring up the chat dialog window and type in */explain*.
![explain webscraper.py](./images/ct51.png?raw=true "explain webscraper.py")   

5. This will dump a lot of output in the dialog. To better review it, click on the *View in Chat* button to put it in the main Chat interface.
![view in chat](./images/ct52.png?raw=true "view in chat")   

6. In the chat interface, you can scan through the output if you want, but you don't have to. It is interesting to go back up to the top of the output, and expand the "Used ## references" section to see the references that Copilot used in providing the explanation.
![view in chat](./images/ct53.png?raw=true "view in chat")

7. While we're at it, let's have Copilot explain how the testing file it created for us works. In the chat interface - enter *@workspace /explain # and pause. There should then be a popup, where you can select the *#file* entry.
```
@workspace /explain #
```
![selecting file](./images/ct54.png?raw=true "selecting file")

8. After you selecting the *#file* selector, you should get a popup near the center top of the codespace interface. This will let you select the *test_webscraper.py* file. Select that file.
![selecting file](./images/ct55.png?raw=true "selecting file")

9. You'll then have a highlighted command to explain the file. Hit Enter for that. You may then have another popup to select the range of the testing file to explain. If so, you can just select the *TestWebScraper* entry.
 ![full entry](./images/ct57.png?raw=true "full entry")
 ![full entry](./images/ct56.png?raw=true "full entry")  

10. After executing this, you'll likely see some updated code suggestions, but you can scroll down further to see the *Explanation* section.
 ![explanation](./images/ct58.png?raw=true "explanation") 

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 2 - Using Copilot to create tests**

**Purpose: In this lab, we'll see how to have Copilot create tests for us.**

1. Let's see how to use the shortcut command */tests* to generate some tests. Still working with the same prime.py file, highlight the code and use the *CMD+I* shortcut to bring up the inline chat dialog. In the text entry box for the dialog, enter the */tests* command.

![using the shortcut command to gen tests](./images/ct07b.png?raw=true "using the shortcut command to gen tests")

2. After running the command, Copilot generates some basic assert-based tests. The tests may first be shown in a pop up dialog window. You can add them into a separate file by accepting them using the the checkmark control in the upper right of the dialog.

![proposed tests from slash command](./images/ct08.png?raw=true "proposed tests from slash command")

3. We can also get the same results from invoking the *Generate Tests* entry from the context menu. Try that now by going back to the *prime.py* file highlighting the code, right-clicking on it, then selecting *Copilot* and then *Generate Tests*. Since we already have tests generated from the other command, you can just close this dialog.

![proposed tests from the menu](./images/ct09b.png?raw=true "proposed tests from the menu")

4. Let's see what other suggestions Copilot can come up with for tests. In the new file that was created, highlight the tests and then hit **Ctrl+Enter** to see other possible completion options. 

![scrolling through alternative options](./images/ct10.png?raw=true "scrolling through alternative options") 

5. It is doubtful that Copilot will produce an alternative that is better than what you have, but if you want, you can pick a different option by clicking on the **Accept suggestion #** button under the suggestion. 

6. We can also use comments to have Copilot create tests. Let's try this in the original *prime.py* file. Under the code, add a comment line that tell Copilot to create tests for the code above.
```
# Create tests for the code above
```

7. Hit return (if you haven't) and Copilot will probably supply a generic testing routine, such as below (NOTE: if you only get the first line, you may need to "nudge" Copilot by typing "result" or similar after accepting the first line):
```
def test_is_prime(number, expected):
    result = is_prime(number)
    assert result == expected, f"Expected {expected} but got 
{result}"
```

8. Depending on your particular comment and context, Copilot may produce a more generic testing function or a set of individual test cases. To ensure you get the latter,  delete the generated code from the previous comment and redo the steps with this comment. (You may need to hit return again and give Copilot a few seconds to generate the tests.)

```
# Create a set of 10 unit tests for the code above
```

9. In this case, Copilot will usually generate a more explicit set of tests wrapped in a testing function. An example is shown next.
![test by comment](./images/ct14.png?raw=true "test by comment")    

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 3 - Generating tests through code suggestions and corrections**

**Purpose: In this lab, we'll see how to have Copilot finish tests for us using code suggestions and corrections.**

1. To get started using this approach, you need to remove the existing testing code (if any, in the prime.py file) and delete all blank lines under it. Then start typing the start of a testing function, but just the first line.
```
def test_is_prime(number):
```

2. Copilot may show a suggestion for completion, but we'll ignore that for now. Click in a different window outside of the file editor.  There should be a red wavy line showing on the last line of the file. This means there's an issue with the code.
![error in function](./images/ct15.png?raw=true "error in function") 

3. There should be an AI symbol (the two stars) showing up in the listing. Click on that and you should get an option to have Copilot fix the problem.
![option to fix error](./images/ct16.png?raw=true "option to fix error") 

5. Copilot has likely generated a simple if/else code path to print whether or not the function passed. This is not what we really need, so you can just *Discard* the suggestion. (Or if you've already accepted it, you can just select and erase that code.)
![error in function](./images/ct17.png?raw=true "error in function") 

6. To get something more direct (like specific use cases), we can add additional tokens and/or keywords to the context. Let's add an *assert* keywork and then let Copilot suggest the remaining part of the test. In the *test_is_prime* function, add an *assert* statement underneath as shown below. Then you can accept the suggestion.

![start with assert](./images/ct18.png?raw=true "start with assert")   

6. From here, you can continue with the Enter/Tab key sequences to get a set of assertion tests.

7. While this is an ok set of basic tests, we'd like to ensure better coverage. Let's ask Copilot about any other edge cases. Enter the prompt below into the chat window. Copilot should respond with an explanation of different edge cases and sample code for the tests.
```
are there any other edge cases that should be tested?
```
![edge cases generation](./images/ct38.png?raw=true "edge cases generation")   

8. We can now copy the example test cases and add them to our testing file via the usual chat methods. (Hover over output, copy it, and paste/insert into the testing file we previously created).

![edge cases insert](./images/ct39.png?raw=true "edge cases insert")   

9. Let's go ahead and have Copilot document our test cases here. Highlight the test cases and then, using the Cmd+I dialog, enter the shortcut command */doc*. You can accept the suggested documentation if you're happy with it.
<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 4 - Validating Inputs**

**Purpose: In this lab, we'll see how to have Copilot help validate inputs in functions.**

1. Copilot can also help with other kinds of validation besides general test cases. It can also validate that inputs going into a function are valid. Highlight your *is_prime* code and enter the prompt below into the Copilot Chat interface.

```
generate asserts to ensure that the inputs to the function are valid
```

2. From here, Copilot should respond and suggest asserts, as requested, to validate the functions inputs. The response may look something like the following (again you do not have to change anything).

![validating inputs with asserts](./images/ct40.png?raw=true "validating inputs with asserts")   
```
(From Copilot:)

To ensure that the function inputs are valid, we can add assertions
at the start of the function. We want to make sure that the input 
is an integer and that it is not negative. Here's how you can do it:


def is_prime(num):
    assert isinstance(num, int), "Input must be an integer"
    assert num >= 0, "Input must be a non-negative integer"

    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```
3. We can also be less specific about using asserts and ask Copilot to generate checks. Try this prompt:
```
generate checks to ensure that the inputs to the function are valid
```

4. This should allow Copilot to generate code to validate the inputs, but with a more standard coding mechanism to surface any issues. Here's what example output from that might look like.

![validating inputs with checks](./images/ct41.png?raw=true "validating inputs with checks")  
```
To ensure that the inputs to the `is_prime` function are valid, you
can add checks at the start of the function.
 Here's how you can do it:

python
def is_prime(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num < 0:
        raise ValueError("Input must be a non-negative integer")

    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


In this code, the `if` statements will raise a `TypeError` if the
 input is not an integer or a `ValueError` if it's a negative 
number.
 This way, you can ensure that the inputs to the function are valid.
```

5. When you're happy with this code, you can go ahead and add them to your code using the options in the code window of the chat.
![validating inputs with checks](./images/ct42.png?raw=true "validating inputs with checks")  

6. While we are discussing inputs, we should also consider other types of inputs to test for. Switch back to the file with the test cases and have it open in the editor. Now let's prompt Copilot to look at these and consider any other types of inputs. Enter ther following prompt:
```
Referencing #editor, add test cases for other types of inputs
```

7. With this prompt, Copilot will likely add some additional test cases like these.
   
```
    def test_float_input(self):
        with self.assertRaises(TypeError):
            is_prime(7.1)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            is_prime("7")
```

8. Go ahead and hover over the output and add them to the file with the test cases.
![adding test cases for different input types](./images/ct43.png?raw=true "adding test cases for different input types")  

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 5 - Leveraging frameworks and TDD**

**Purpose: In this lab, we'll see how to leverage Copilot with testing frameworks and how to do Test-Driven Development with it.**

1. Let's look at a TDD approach of creating the test cases with a failing test and then immplementing the code to be tested. Consider a simple example where we want to create a test class and tests for students at a university. We'll use Mockito as our testing framework. Let's have Copilot create a pom.xml file for us with a mockito dependency. In the separate chat interface, enter the following prompt:
```
add a pom.xml file with a mockito dependency, and compiler source and target version 1.8
```
![add pom with mockito dependency](./images/ct33.png?raw=true "add pom with mockito dependency")  

2. Now, let's put the generated content into a new file in our project. Hover over the generated code, select the *... (More actions)* at the end and then click on *Insert into New File*. Then save the file as *pom.xml* via the *3 bar* menu in the upper left, then *File*, then *Save As..*. 

![insert into new file](./images/ct34.png?raw=true "insert into new file")  
![save file](./images/ct29.png?raw=true "save file") 

3. Now, let's create an appropriate test class and initial set of tests. Do this in the Copilot separate Chat interface, since we expect a significant amount of output and we may want to put it in a separate file. We'll use a prompt that tells Copilot to focus on the *pom.xml* file we just created.
```
(In the separate chat interface)
Referencing #file:pom.xml, create a StudentTest class for students enrolled at a university and add tests
```

4. The suggested StudentTest class from this prompt is likely overkill for what we want for a simple test case for a *Student* class. However, Copilot will likely detect that we need the Junit dependency at the start of the output. So let's go ahead and add that into our *pom.xml* file. Save the changes to the pom.xml file afterwards.

![add junit dependency](./images/ct30.png?raw=true "add junit dependency")  
   
5. Let's restructure the prompt to ask for something more specific for the StudentTest class. Enter the following in chat.
```
(In the separate chat interface)
Referencing #file:pom.xml, create only a StudentTest class for a student enrolled at a university. A student will have personal attributes such as a first and last name, a phone number, an address, and a contact email. The StudentTest class should be part of a com.example package.
```
![more specific query to create tests](./images/ct21.png?raw=true "more specific query to create tests")  

6. The output from Copilot now likely looks more like what we wanted as a starting point. Click into the output for the *StudentTest* class, hover over the top right, and use the icon (or copy and paste) to put it in a different file. Save the file as **src/test/java/com/example/StudentTest.java**.
![save new test](./images/ct31.png?raw=true "save new test")

7. Now, let's execute Maven to try the testing. (Note: We expect it to fail because we don't have the *Student* class implemented yet.)

```
mvn test
```
![initial test](./images/ct32.png?raw=true "initial test")


8. Folllowing the TDD methodology, let's next create the minimum code to make this test pass. We can use Copilot for that. Make sure the *StudentTest.java* file is open in the editor, and then use this prompt to create the code.
```
(in the separate Chat interface)
Referencing #editor, create a student class with verbose comments.
```
![output of query to create student class with comments](./images/ct35.png?raw=true "output of query to create student class with comments")

9. As we did before, hover over the output, insert the code into a new file. Then save it as **src/main/java/com/example/Student.java**

![saving student file](./images/ct36.png?raw=true "saving student file")

10. Finally, let's run the test again and it should pass. 
```
mvn test
```
![run test and see it pass](./images/ct37.png?raw=true "run test and see it pass")


<p align="center">
**[END OF LAB]**
</p>

<p align="center">
**THANKS!**
</p>
 

