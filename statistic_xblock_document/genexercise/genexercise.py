"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import os
from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment


class GenexerciseXBlock(XBlock):
    """
    XBlock to show exercise which add my teacher,show json data into html.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the GenexerciseXBlock, shown to students
        when viewing courses.
        """

        """
        pull answer files from gitlab
        """
       # os.system('/var/www/zyni/script/pullFromGitlab.sh')

        """
        statistic according to answer files
        """
       # os.system('python /var/www/zyni/script/statistic.py')

        """
        push result to github
        """
       # os.system('/var/www/zyni/script/pushToGitHubStatistic.sh')
        
        html = self.resource_string("static/html/genexercise.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/genexercise.css"))
        frag.add_javascript(self.resource_string("static/js/src/genexercise.js"))
        frag.initialize_js('GenexerciseXBlock')
        return frag

    def studio_view(self, context=None):
        """
        The studio view of the GenexerciseXBlock, shown to teacher
        when add exercise
        """
       
        html = self.resource_string("static/html/genexercise_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/genexercise.css"))
        frag.add_javascript(self.resource_string("static/js/src/genexercise_edit.js"))
        frag.initialize_js('GenexerciseXBlock')
        return frag  

    @XBlock.json_handler
    def statistic_click(self,data,suffix=''):
        os.system('/var/www/zyni/script/pullFromGitlab.sh')
        os.system('python /var/www/zyni/script/statisticNewAdded.py')
        return {"data":"success"}
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("GenexerciseBlock",
             """<vertical_demo>
                <genexercise/>
                <genexercise/>
                <genexercise/>
                </vertical_demo>
             """),
        ]
