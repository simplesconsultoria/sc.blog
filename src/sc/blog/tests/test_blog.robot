*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Test cases ***

Create Blog, subobjects and test views
    Enable Autologin as  Site Administrator
    Go to Homepage

    # create a blog without image
    Open Add New Menu
    Click Link  css=a#blog
    Page Should Contain  Add Blog
    Input Text  css=#form-widgets-IDublinCore-title  It's a Blog
    Input Text  css=#form-widgets-author  HJS

    Click Button  Save
    Page Should Contain  Item created

    # verify the blog header is visible
    Element Should Be Visible  css=#blog-header
    # check the title is visible
    Element Should Be Visible  css=.documentFirstHeading

    # edit the blog and add an image
    Click Link  link=Edit
    Choose File  css=#form-widgets-image-input  /tmp/img1.jpg
    Click Button  Save
    Page Should Contain  Changes saved

    # check the title is now an attribute of the image
    Element Should Be Visible  xpath=//img[@title="It's a Blog"]
    Element Should Be Visible  xpath=//img[@alt="It's a Blog"]

    # add a post
    Open Add New Menu
    Click Link  css=a#document
    Page Should Contain  Add Page
    Input Text  css=#title  It's a Post
    Click Button  Save
    Page Should Contain  Changes saved

    # verify the post is listed in the blog
    Click Link  link=It's a Blog
    Page Should Contain  It's a Post

    # open the post
    Click Link  link=It's a Post
    # verify the blog header is visible
    Element Should Be Visible  css=#blog-header

    # create a folder
    Click Link  link=It's a Blog
    Open Add New Menu
    Click Link  css=a#folder
    Page Should Contain  Add Folder
    Input Text  css=#title  SubFolder
    Click Button  Save
    Page Should Contain  Changes saved

    # create a post inside the folder
    Open Add New Menu
    Click Link  css=a#document
    Page Should Contain  Add Page
    Input Text  css=#title  It's a SubPost
    Click Button  Save
    Page Should Contain  Changes saved

    # verify the second post is listed in the blog
    Click Link  link=It's a Blog
    Page Should Contain  It's a Post
    Page Should Contain  It's a SubPost

    # open the second post
    Click Link  link=It's a SubPost
    # verify the blog header is visible
    Element Should Be Visible  css=#blog-header

    # change the blog view
    Click Link  link=It's a Blog
    Open Display Menu
    Click Link  css=a#plone-contentmenu-display-blog_summary_view

    # verify the new view
    Page Should Contain  It's a Post
    Page Should Contain  It's a SubPost

    # delete the blog
    Open Action Menu
    Click Link  css=a#plone-contentmenu-actions-delete
    Click Button  Delete
    Page Should Contain  Plone site
    Go to Homepage
    Page Should Not Contain  It's a Blog
