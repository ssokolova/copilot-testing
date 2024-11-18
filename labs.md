# Automating Testing with GitHub Copilot
## Revision 3.0 - 11/18/24

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**NOTE: To copy and paste in the codespace, you may need to use keyboard commands - CTRL-C and CTRL-V.**

**Lab 1 - Using Copilot to create tests**

**Purpose: In this lab, we'll see basic ways to have Copilot create tests for us.**

1. In our repository, there is an example Python file named *prime.py* that we'll be starting with. You can open it by clicking on [**prime.py**](./prime.py) , or, in the terminal, enter

```
code prime.py
```

2. Let's see how to use the shortcut command */tests* to generate some tests. In the same prime.py file, highlight the code and use the *CMD+I* shortcut to bring up the inline chat dialog. In the text entry box for the dialog, enter the */tests* command and click on the arrow on the right at the end to submit it.

![using the shortcut command to gen tests](./images/new-slash-tests-command.png?raw=true "using the shortcut command to gen tests")


3. After running the command, Copilot generates some basic assert-based tests in a new file. You can just save this file as *test_prime.py*. To do this, click on the *3-bar* menu in the upper left corner of the codespace, then click *File*, then *Save As* (or use the menu shortcut). Reply yes to the dialog asking about saving AI-generated results.
   
![proposed tests into new file](./images/new-slash-tests-output.png?raw=true "proposed tests into new file")
![saving file](./images/new-slash-tests-save-output-as-new-file.png?raw=true "saving file")

   
4. We can also get the same results from invoking the *Generate Tests* entry from the context menu. Try that now by going back to the *prime.py* file highlighting the code, right-clicking on it, then selecting *Copilot* and then *Generate Tests*. Since we already have tests generated from the other command, you can just close this dialog. (Note: If you don't see any tests generated this way, try closing the test-prime.py file and run again.)
   
![proposed tests from the menu](./images/new-tests-generated-from-menu.png?raw=true "proposed tests from the menu")

5. We can also use comments to have Copilot create tests. Let's try this in the original *prime.py* file. Under the code, add a comment line that tells Copilot to create tests for the code above.

```
# Create tests for the code above
```

![tests from comments](./images/ct74.png?raw=true "tests from comments")

6. Hit return (if you haven't). Copilot may supply a generic testing routine, such as below, the start of a routine, or a set of actual assert-based tests (NOTE: if you only get the first line, you may need to "nudge" Copilot by typing "result" or similar after accepting the first line):

```
def test_is_prime(number, expected):
    result = is_prime(number)
    assert result == expected, f"Expected {expected} but got 
{result}"
```

7. Depending on your particular comment and context, Copilot may produce a more generic testing function or a set of individual test cases. To ensure you get the latter,  delete the generated code from the previous comment and redo the steps with this comment. (You may need to hit return again and give Copilot a few seconds to generate the tests.)

```
# Create a set of 10 unit tests for the code above
```

8. In this case, Copilot will usually generate a more explicit set of tests wrapped in a testing function. An example is shown next.

![test by comment](./images/ct14.png?raw=true "test by comment")    

<p align="center">
**[END OF LAB]**
</p>
</br></br>


**Lab 2 - High-level Copilot Testing Advice**

**Purpose: In this lab, we’ll start to learn about getting more general assistance from Copilot for testing**

1. In our repository, there is an example Python file we'll be using to start with. You can open it by clicking on [**webscraper.py**](./webscraper.py) , or, in the terminal, enter

```
code webscraper.py
```
 
2. Let's ask Copilot for some general testing advice for this code. Switch to the separate chat area, and ask it:

```
How can I test #file:webscraper.py?
```

![query in chat](./images/ct80.png?raw=true "query in chat")

3. Copilot will likely have generated some output with a set of instruction and some example code similar to what's shown below. Notice that it brings in a unit testing framework. The generated code may not be complete - for example, it may have *placeholders* for input and output data.
   
![testing suggestions for file](./images/ct45.png?raw=true "testing suggestions for file")

4. Let's take the generated code and put it into a new file. Hover over the code section, and click on the 3 dots at the end of the popup bar.
   
![hover](./images/ct46.png?raw=true "hover")

5. From the menu that pops up, select the *Insert into New File* option and insert the code into a new file in the project.

![insert into new file](./images/ct47.png?raw=true "insert into new file")

6. Now, select the file, and save it. You can use the 3 bar menu on the left, then File->Save and save it as *test_webscraper.py*.

![saving as new file](./images/ct75.png?raw=true "saving as new file")

7. Let's also look at how we can add code coverage information for the file. Select the *webscraper.py* file in the editor. Then, switch to the separate chat dialog and type the question in there. After you hit Enter, you should see some info from Copilot on how to do coverage.

```
How can I measure code coverage on this file?
```

![query on code coverage](./images/ct76.png?raw=true "query on code coverage")

8. Near the bottom of this output, you may see some *Example Commands in Sequence*. If so, hover over them and click the icon that looks like a terminal to send these commands directly to the terminal. (If you don't see a group, you can still hover over the individual commands, and insert them one at a time into the terminal via the popup terminal icon.)

![query on code coverage](./images/ct77.png?raw=true "query on code coverage")

9. When you click on that terminal icon, it should populate the terminal with those commands and you can run them. While there will be coverage numbers generated, they will not be accurate or complete, because our code doesn't currently run.
![coverage results](./images/ct78.png?raw=true "coverage results")

10. Finally, let's have Copilot help us identify any other edge cases that we should consider. Switch back to the *test_prime.py* file, highlight the text, and then, in the Chat interface, enter the prompt "Are there any other edge cases that should be tested?".

```
Are there any other edge cases that should be tested?
```

![finding other test cases](./images/ct81.png?raw=true "Finding other test cases")

11. This should result in some additional test cases being generated in Chat that you can then just replace in the *test_prime.py* file by using the *Insert at Cursor* icon that shows up when you hover over the code.

![adding test cases](./images/ct82.png?raw=true "Adding test cases")

    
<p align="center">
**[END OF LAB]**
</p>
</br></br>


**Lab 3 - Using other Copilot features to help with testing**

**Purpose: In this lab, we'll see how to leverage some of Copilot's other features to help with testing**

1. Let's see how the Copilot Fix functionality can help us out. Click on/open the *test_prime.py* file from the earlier labs. At the top, let's add a new import. Type in the line below.
```
import pytest2
```

2. You may already know that this is not a valid import, but let's assume we've tried to use it and it failed. So, let's see if Copilot can help identify and correct the issue for us. Select/highlight *pytest2* and then right-click and select *Copilot* from the menu. Then select *Fix this* from the submenu.
   
![copilot fix](./images/ct83.png?raw=true "Copilot fix")

3. Copilot should recognize that this is not a valid import and then suggest a correction/fix that you can then *Accept* from the dialog. (The suggested fix may be to *import pytest* or it may be to remove the line altogether.)

![copilot fix](./images/ct84.png?raw=true "Copilot fix")


4. Next, let's try out the Copilot */tests* shortcut command with a different kind of file and language. There's a large demo file of SQL statements in this project named [**create-tables.sql**](./create-tables.sql). Open that.

```
code create-tables.sql
```

5. Since this is a different type of file, we will specify the filename when we ask Copilot to generate tests this time. Enter the following question in the chat interface. It will automatically add an *@workspace* participant at the start - delete the "@workspace" part.

```
/tests #file:create-tables.sql
```

6. Copilot should respond with some overall instructions/plan and suggested examples of how to do the steps. You can just review these to see the example, you don't need to do anything with them.

![testing suggestions for SQL](./images/ct06.png?raw=true "testing suggestions for sql")   

7. Suppose we need to better understand the code we're testing. We can have Copilot explain the code to us. Highlight all of the code in the file *webscraper.py* and then use the CMD/CTRL+I shortcut to bring up the chat dialog window and type in */explain*.

![explain webscraper.py](./images/ct51.png?raw=true "explain webscraper.py")   

8. This will dump a lot of output in the dialog. To better review it, click on the *View in Chat* button to put it in the main Chat interface.

![view in chat](./images/ct52.png?raw=true "view in chat")   

9. While we're at it, let's have Copilot explain how the testing file it created for us works. In the chat interface - enter *@workspace /explain # and pause. There should then be a popup, where you can select the *#file* entry. (You may have to use the arrow keys to select it.)

```
@workspace /explain #
```

![selecting file](./images/ct54.png?raw=true "selecting file")

10. After you selecting the *#file* selector, you should get a popup near the center top of the codespace interface. This will let you select the *test_webscraper.py* file. Select that file.

![selecting file](./images/ct55.png?raw=true "selecting file")

11. You'll then have a highlighted command to explain the file. Hit Enter for that. You may then have another popup to select the range of the testing file to explain. If so, you can just select the *TestWebScraper* entry.
 
 ![full entry](./images/ct57.png?raw=true "full entry")
 
 ![full entry](./images/ct56.png?raw=true "full entry")  

12. After executing this, you'll likely see some updated code suggestions, but you can scan through to see the sections with explanations.

 ![explanation](./images/ct58.png?raw=true "explanation") 

<p align="center">
**[END OF LAB]**
</p>
</br></br>


**Lab 4 - Documentation for Testing**

**Purpose: In this lab, we'll see how to use Copilot to help document content for testing.**

1. To have the testing code be able to be maintained, it should be documented well. We can have Copilot do this for us too. In the editor, switch to the *test_webscraper.py* file and highlight the code. Open the shortcut dialog with CTRL/CMD+I and enter the */doc* command in it. 

```
/doc
```

 ![using doc shortcut](./images/ct59.png?raw=true "using doc shortcut") 

2. Hit Enter and you'll see some documentation suggested at the start of the file. You can just go ahead and accept that.
 
 ![initial doc suggestion](./images/ct60.png?raw=true "initial doc suggestion")

3. This is useful, but we'd like to have the test cases more thoroughly documented. Bring up the chat dialog again with the CTRL/CMD+I sequence and tell Copilot in the dialog to "verbosely comment all the code so it's easy to understand".

```
verbosely comment all the code so it's easy to understand
```

 ![verbose doc prompt](./images/ct63.png?raw=true "verbose doc prompt")

4. Hit Enter and you should more thorough comments suggested throughout the code body. You can go ahead and *Accept* them.

![verbose doc suggestions](./images/ct64.png?raw=true "verbose doc suggestions")


5. While we're working with documentation, sometimes it can be useful to have documentation on features like APIs to go off of. Let's have Copilot try to generate that for us. In the chat interface, enter "Create API documentation for the APIs in #file:webscraper.py". After hitting Enter, you should eventually see some documentation for the APIs in among other output.

```
create API documentation for the APIs in #file:webscraper.py
```

![api doc](./images/ct65.png?raw=true "api doc")


6. Before we do the remaining steps, let's start a new Chat session. Back in the left side Chat window, click the "+" sign at the top to start a new session.

![new chat](./images/ct85.png?raw=true "New chat")


7. Let's try one more doc step here. Let's have Copilot generate functional documentation to help us understand the code we're testing. In the chat interface, enter in the prompt "Create functional documentation for the #file:webscraper.py" and hit Enter. Copilot should then generate extensive documentation with the details of the file.

```
create functional documentation for the #file:webscraper.py
```

![functional doc](./images/ct66.png?raw=true "functional doc")


8. Having this documentation generated in Copilot is useful, but to make it more widely sharable we need to be able to save it separately. Simply copying it from the Chat interface won't preserve any generated code. To ensure you get everything, it works best to click on the "..." menu in the upper right of the Chat section and select "Open Chat in Editor". Go ahead and do that now.

![open chat in editor](./images/ct67.png?raw=true "open chat in editor")


9. In the copy of the chat that is open in the editor now, you can right-click and select *Copy All*. This will copy all the content. 

![copy markdown](./images/ct68.png?raw=true "copy markdown")


10. You can then paste this into a text file, save it as .md (markdown) format and then view it in a markdown viewer or convert it.

![copy markdown](./images/ct69.png?raw=true "copy markdown")

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 5 - Validating Inputs**

**Purpose: In this lab, we'll see how to have Copilot help validate inputs in functions.**

1. Copilot can also help with other kinds of validation besides general test cases. It can also validate that inputs going into a function are valid. Go back to the *prime.py* file, highlight your *is_prime* code and enter the prompt below into the Copilot Chat interface.

```
generate asserts to ensure that the inputs to the function are valid
```

2. From here, Copilot should respond and suggest asserts, as requested, to validate the functions inputs. The response may look something like the following (again you do not have to change anything).

![validating inputs with asserts](./images/ct40.png?raw=true "validating inputs with asserts")   

3. We can also be less specific about using asserts and ask Copilot to generate checks. Try this prompt (again in the Chat interface):

```
generate checks (without using asserts) to ensure that the inputs to the function are valid
```

4. This should allow Copilot to generate code to validate the inputs, but with a more standard coding mechanism to surface any issues. Here's what example output from that might look like.

![validating inputs with checks](./images/ct41.png?raw=true "validating inputs with checks")  


5. When you're happy with this code, you can go ahead and replace the highlighted code in the file using the options in the code window of the chat.

![validating inputs with checks](./images/ct42.png?raw=true "validating inputs with checks")  

6. While we are discussing inputs, we should also consider other types of inputs to test for. Switch back to the *test_prime.py* file with the test cases and have it open in the editor. Now let's prompt Copilot to look at these and consider any other types of inputs. Enter ther following prompt:

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

9. Finally, as long as we're here, let's see if Copilot can help refactor our code to make it more testable. Enter the query below in the Chat interface. After the results are shown, you can go ahead and use them to replace your code if you want.

```
Refactor the code in #file:prime.py to make it more easily testable
```

![Refactoring for testing](./images/ct72.png?raw=true "refactoring for testing")  

10. You can do the same thing for the webscraper.py file.
Enter the query below in the Chat interface. After the results are shown, you can go ahead and use them to replace your code if you want.

```
Refactor the code in #file:webscraper.py to make it more easily testable
```

![Refactoring for testing](./images/ct73.png?raw=true "refactoring for testing")  


<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 6 - Leveraging frameworks and TDD**

**Purpose: In this lab, we'll see how to leverage Copilot with testing frameworks and how to do Test-Driven Development with it.**

1. Let's look at a TDD approach of creating the test cases with a failing test and then immplementing the code to be tested. Consider a simple example where we want to create a test class and tests for students at a university. We'll use Mockito in our testing framework. Let's have Copilot create a pom.xml file for us with a mockito dependency. In the separate chat interface, enter the following prompt:

```
add a pom.xml file with a mockito dependency version 3.3.3, and compiler source and target version 1.8
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

4. The suggested StudentTest class from this prompt is likely overkill for what we want for a simple test case for a *Student* class. However, Copilot will likely detect that we need the Junit dependency at the start of the output. There will likely be a step or segment of code to *update pom.xml with JUnit dependencies* at the top or bottom of the output. So let's go ahead and add that part only into our *pom.xml* file. (You can just have the **corresponding section** of the pom.xml file contents highlighted and then *Insert At Cursor* to replace it.) Save the changes to the *pom.xml* file afterwards.

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
[END OF LAB]
</p>

<p align="center">
THANKS!
</p>
 

