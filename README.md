<h3 align="center">Hacker Rank Solutions</h3>

<h4>Absract : </h4>
</br>
<p> HackerRank is one of the most popular platforms to practice coding and improve our programming skills.
Many times people need solutions to the problems which is available in various locations, one has to search in places like others GitHub, some blogpost websites, etc.., and those websites do not have solutions to all the problems in hackerrank and does not even have a search bar to get the desired solutions.

So We came up with an idea to build a web application with "Django" having a search bar and sections( where people can choose the domain like python, java, data structures, problem-solving, etc .. as in hackerrank) which is a one place to get all the solutions to all the problem statements in hackerrank.

We have an internal search bar,so that people can easily find the required solution by just specifying their problem title or a part of the problem statement. For the general domains like data structures and problem solving, solution is provided in 4 languages;  Java, C , C++ and python.

The Website is completely responsive and flexible on all types of devices.
We have even enabled the pagination bar to navigate between the pages.
We also used django allauth SocialAccounts library to enable login with google(google auth API)
</p>

</br>
<h4>Tech Stack : </h4>
</br>
<p>Django, html, css, simple Js, Heroku for deployment and Pycharm IDE for holding all the things compact</p>

</br>
<h4>To run our application on your local machine :</h4>
</br>
<p>
step 1: clone your repo from https://github.com/pychampsHackathon/djangowebsite-pychamp
step 2: navigate to the cloned folder
step 3: activate the HackerRankEnv 
             if windows source HackerRankEnv/Scripts/activate
             if mac/linux  source/bin/activate
step 4: navigate to root of project by  "cd HackerRank"
step 5: run >> python3 manage.py runserver

if you get any requirements error
just run pip3 install -r requirements.txt in the same location where manage.py exists </p>