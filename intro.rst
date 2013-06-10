Introduction
============

Why am I writing this?
----------------------

Python programming is the most useful scientific tool that I've learned
outside of chemistry laboratory skills. Spreadsheet programs, such as MS
Excel, are capable tools that serve a useful role for many scientists;
however, there are a number of reasons that it can be advantageous to learn a
programming language as a compliment to a spreadsheet-based software. First of
all, simple programs can automate many of your repetitive data analysis tasks.
In addition, knowing a programming language can be helpful for specialized
data analyses, and with your programming skills, you have the ability to
create your own custom tools for the job. As a bonus, learning to program can
be an enjoyable pastime that also provides you with a clearer understanding of
computer terminology and processes.

I started teaching myself Python in 2007, and at the time, I found a near
infinite number of introductory tutorials on the web and books made of paper.
Unfortunately, most of these reference materials are geared towards computer
scientists and professional programmers, so I spent a substantial amount of
time determining how to apply these concepts to my data analysis problems.
This meant that, compared with a program like Excel, I was not able to
productively apply this knowledge for quite some time. Below is a graphical
productivity versus time investment comparison of Excel and Python from my
personal experience.

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(1, 10, 1000)
    
    plt.plot(x, np.log(x), lw=2, label='Excel')
    plt.plot(x, np.exp(x)/2000., lw=2, label='Python')

    plt.xlabel('Time Investment', fontsize=16)
    plt.xticks( [] )
    
    plt.ylabel('Productivity', fontsize=16)
    plt.yticks( [] )

    plt.legend(loc=2)
    plt.show()


I wrote this document as a way for new users to learn Python programming in a
more efficient manner. As a more experienced Python programmer, I now realize
that many of the tasks I wanted to accomplish did not require an exhaustive
understanding of the language.  Other tutorials proceed in step by step manner
with substantial detail spent on each subtopic.  This is a useful approach to
learning but is also very time consuming.  In this introduction, topics will
be presented in the context of real world examples. Each of these examples
will require a slightly different skill set, so new concepts, terminology, and
third party packages will be presented as needed to get you up and running as
quickly as possible.  My hope is that that this modified pedagogical approach
will improve your learning curve, making it more along the lines of using a
spreadsheet-based program (see below). Unfortunately, using a programming
language will never be as 'easy' as a spreadsheet, but you'll see that the
analysis power gained using programming techniques will far outweigh the time
costs.

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt
    
    x = np.linspace(1, 10, 1000)
    
    plt.plot(x, np.log(x), lw=2, label='Excel')
    plt.plot(x, np.exp(x)/2000., lw=2, label='Python')
    plt.plot(x, np.log(x)/2. + np.exp(x)/2300., lw=2, label='This Tutorial')
    
    plt.xlabel('Time Investment', fontsize=16)
    plt.xticks( [] )
    
    plt.ylabel('Productivity', fontsize=16)
    plt.yticks( [] )
    
    plt.legend(loc=2)
    plt.show()


Why Choose Python?
------------------

There are many, many programming languages, so an obvious question is "Why
choose Python?". First of all, Python was designed with readability as a
primary goal. As such, Python code is easier to read than almost any other
programming language. Python has a minimal syntax with very few special
characters (brackets, semicolons, etc.), and it enforces some structural
uniformity, specifically indentation, to improve code appearance. A downside
of these structural rules is a small lack of flexibility that can take some
getting used to; however, given some practice, these constructs will become
second nature.  This readability standard makes Python code extremely rapid to
write as well. This means that you will spend less time processing your data
and more time on interpretation and analyses.

In addition, Python comes with an interactive interpreter that allows you to
test code snippets and track what is happening to your data. This means that
you don't have to write your entire program to see if things are working.  You
can check different segments of code and track the results without having to
do all of the work in advance. A third-party advanced interpreter (:ref:`ipy`)
is also available that takes the interactive coding experience to a new level.

One of the most important aspects of Python, from our point of view, is its
large and active scientific user base. In my opinion, scientific users are
drawn to Python by the advantages outlined above, and the fact that it is open
source is important for future reproducibility (a fact that can sometimes be
overlooked when you are using proprietary software).  These users have
contributed huge amounts of freely-available code , which can be used as a
base for all of your scientific needs.  See :doc:`Appendix A
<./appendix_a/appendix_a>` for a partial listing of some of these third party
add-on packages for various scientific disciplines.

Practice Makes Perfect
----------------------

Duh. You will not learn anything by passively reading this material. It is
essential that you actually work through these examples.  In addition, find a
project that you would like to tackle for your own research. Forcing yourself
to apply this to something that is important to you will really help to
solidify this material in your mind.

External Resources
------------------

This tutorial is not meant to be a comprehensive.  Several reference sites are
highlighted here that are more generally useful than this short document will
ever be.

* `The official Python documentation`_: This is a great resource that you
  should get to know well. It has a nice, short tutorial to the language, and
  a reference for pretty much everything else.
* `Scipy Lecture Notes`_: This may be one of the best tutorials for learning
  Python in a scientific context. These are actively developed reference
  materials and are updated on a somewhat regular basis. I don't like some of
  the organization of the material, but it is a good general reference for
  many of the third party scientific packages that are available for Python.
* `Stackoverflow`_: This is a general programming question/answer site;
  however, it gets very heavy scientific Python traffic. In addition, users
  can vote on the answers they like best, making it pretty easy to find the
  most useful information.
* `Google`_: Sometimes you just gotta Google that thing. Use this frequently.
  Before you seek out advice from a peer or mailing list, type your question
  into Google verbatim. You might be surprised what you find.

.. References

.. _The official Python documentation: http://docs.python.org/2/
.. _Scipy Lecture Notes: http://scipy-lectures.github.io/ 
.. _Stackoverflow: http://stackoverflow.com/
.. _Google: http://google.com
