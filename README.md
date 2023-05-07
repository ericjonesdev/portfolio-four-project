# A Coder's Journey - A Journey Into Software Development

<a href="https://a-coders-journey.herokuapp.com/">View the live page here</a>

A coder's Journey is a web application which serves as a database & online
community of people interested in the particulars related to software development,
entreprenuership, and learning. The site aims to be a living document of user and
admin expertise, as it relates to the ins-and-outs of software engineering.

The site is constructed as a user-friendly blog/newssite where users can view,
comment on, create and like blog posts. General users are able to exercise CRUD
functionality, as it pertains to their individual profile, with the abilities to
read, update and delete their own profile.

Admin users are able to manage all CRUD functionalities within the site, as well
as search post information by username, date create and slug information. The
overall structure and asthetic of A Coder's Journey is modeled on the I Think
Therefore I Blog Code Institute Walkthrough.

![homepage](https://res.cloudinary.com/dxla1usfm/image/upload/v1683476837/readme/homepage_evia1w.png "homepage")

## Index - Table of Contents

< table of contents >

### User Experience (UX)

#### User Stories:

- EPIC 01: Registration and Account Management
  <details>
  <summary>User Stories:</summary>

  - US101: Account Registration
    - As a Site User I can register an account so that I can be able to log in and manage my account settings
  - US102: Login and Logout
    - As As a Site user / Admin I can Log in to the site so that I can gain access to my profile and functionalities
  - US103: Profile Page Creation
    - As a Site User I can create my own user profile page so that I can create a short description/bio to showcase to other Site Users
  - US104: Update User Profile
    - As a Site user I can update my profile information so that my information is current and applicable
  - US105: Delete User Profile
    - As a Site user I can delete a user profile so that the user profile is removed from the database

  </details>

- EPIC 02: Viewing and Navigation
  <details>
  <summary>User Stories:</summary>

  - US201: Account Registration
    - As a Site User I can register an account so that I can be able to log in and manage my account settings
  - US202: Login and Logout
    - As As a Site user / Admin I can Log in to the site so that I can gain access to my profile and functionalities
  - US203: Profile Page Creation
    - As a Site User I can create my own user profile page so that I can create a short description/bio to showcase to other Site Users

  </details>

- EPIC 03: Posts and Comments
  <details>
  <summary>User Stories:</summary>

  - US301: View Posts
    - As a Site User I can click on a post so that I can read the full text
  - US302: Comment On a Post
    - As a Site User I can leave comments on a post so that I can be involved in the conversation
  - US303: Like / Unlike a Post
    - As a Site User I can like or unlike a post so that I can interact with the content
  - US304: Like / Create Drafts
    - As a Site User & Site Admin I can create draft posts so that I can finish writing the content later
  - US305: Like / View Post Likes
    - As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral

  </details>

- EPIC 04: Admin and Management
  <details>
  <summary>User Stories:</summary>

  - US401: Approve Comments
    - As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
  - US402: Manage Posts
    - As a Site Admin I can create, read, update and delete posts so that I can manage the blog content
  - US403: Manage Users
    - As a Site Admin I can have full CRUD capability on Users so that manage users on the site

  </details>

### Features

### Existing Features

The following is a breakdown of the primary features of the application. Based
on the 'I Think Therefore I Blog' walkthrough project model, this blog site features
capabilites that are standard for most blog sites.

Any standard feature that is not outlined here, will be included in the 'future build
features' section of this document.

- UX Related Features

  - Fo1 - Consistency among site conten

    Consistency is a key aspect of the website's design, and it extends to the page layout, navigation bar, header, footer, color scheme, and typography. This cohesive approach ensures that the user has a seamless and intuitive experience regardless of which page they're on. Additionally, the navigation bar is responsive to different screen sizes and can be collapsed into a 'burger' menu on smaller screens, further enhancing the user experience.

#### Fig 01-A Desktop example

    ![homepage](https://res.cloudinary.com/dxla1usfm/image/upload/v1683476837/readme/homepage_evia1w.png "homepage")

#### Fig 01-B Mobile example

    ![homepage](https://res.cloudinary.com/dxla1usfm/image/upload/v1683483322/readme/a_coders_journey_mobile_hbiarv.jpg "homepage")

- - Fo2 - Authenticated user indicator

  The user can affirm when they are authenticated (logged in) after successful
  sign up to the site, to which they are taken to the hompage and can view, within
  the navbar at the top, a greyed button with their username within it.

#### Fig 02-A-User Icon upon authentication (signup) to site

- - Fo3 - Home Page

  The application homepage contains a collagae of blog post with stylized post images.
  The site layout gives an introductory view, illustrating to the user what the
  overall them of the site relates to.

#### Fig 03-A-Site Home Page

< homepage pic >

- - Fo4 - View Posts

Users are able to view blog posts on main site and, using 'next' feature link
at the bottom of the page, they are able to view historical posts. When users
create their own post, they are taken to a post list page that shows a history
of their post. If no post have been created, then a banner is displayed to the
user indicating that no post have yet been created.

#### Fig 04-A-List of Blog Posts

< blog post view >

- - Fo5 - Create Post

Users are able to click, within the top navbar profile button, the dropdown and
select to create a post. They are then taken to the create blog post view, where
they are able to format their post via the summernote WSYIWYG editor. Upon click
of the 'create' button, located underneath the post text box area, they are taking
to their individual post list page, which lists their historical posts.

#### Fig 05-A-Create Post View

< create post view >

- - Fo6 - Profile View

From the authenticated user view, a user can click on the '@'<username> portion
of their profile button and be taken to their respective profile page. When using
the profile navbar to click the 'edit profile' choice, they are taken to their
individual edit profile page, where they are able to edit and save their information.

#### Fig 06-A-Create Profile View

< create profile view >

- - Fo7 - Edit Profile

From the authenticated user view, a user can click on the '@'<username> portion
of their profile button and be taken to their respective profile page. When using
the profile navbar to click the 'edit profile' choice, they are taken to their
individual edit profile page, where they are able to edit and save their information.

#### Fig 07-A-Edit Profile

< edit profile view >

- - Fo8 - Comments and Post Likes

Users are able to toggle the heart-shaped like icon, to like or unlike a post. Users
can also submit comments, for review, approval or disproval of the site admin.

#### Fig 08-A-Comments and Likes.

< comments and likes view >

- - Fo9 - Role Based Interactions

Certain functionality is only possible from authenticated users. Likeing a post,
commenting, editing profile and creating a post are reserved for authenticated users
only.

#### Fig 09-A-Options for Authenticated Users.

< logged in user options >

- - F10 - Site Administration

The admin dashboard is only available to the superuser. With this dashboard an
Admin is able to manage users, posts and site structure.

#### Fig 10-A-Site Administration Page

< Site Admin features >

- - F11 - About Us

The about us page gives the user a welcome message, detailing to the user what the
site is about. It also offers a registration link for those who may be interested
in joining the site.

#### Fig 11-A-About Us Page

< About >

- - F12 - Footer

The footer section gives the user access to join the site owners on various social
media platforms, such as Facebook, Twitter, Instagram and Youtube.

#### Fig 12-A-Footer

< Footer >

- How these features support the user stories

  In the User Experience (UX) section of this readme there are 16 user stories
  split between 4 Epics. An additional user story (17 - Social Login) is not included
  within this.

- Features which could be impletemented in the future

  - User functionality

    - Allow the users the ability to delete thier own post

      Having the ability to delete one's own post and/or information is integral
      to great user experience. This would improve site usability.

    - Post, category and user search function

      With the ability to properly search the site, it would create an easier
      navigation, thus increasing viewership.

    - Social Login

      The ability to log on using popular social media accounts provides an ease
      of access and fosters a bigger online community and patronage.

    - Change Password

      Changing a password is sometimes necessary to increase personal, as well as
      site security.

    - Site Chat

      Have an online social chat space can increase the likelyhood of information
      sharing between prospective software engineers and is a sought after
      function on a great deal of blogs.

## Design

### Methodology

- I think Therefore I blog

  This site design and layout used the Code Institute walkthrough and, as such,
  didn't require a wireframe. Although wireframes are useful for prototyping new
  websites, the backend functionality took precedent, due to time constraints.

- Entity-Relationship Diagram for DBMS
