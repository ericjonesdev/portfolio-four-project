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

< main image here >

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

- US Related Features

  - Fo1 - Consistency among site content

  Consistency is a key aspect of the website's design, and it extends to the page layout, navigation bar, header, footer, color scheme, and typography. This cohesive approach ensures that the user has a seamless and intuitive experience regardless of which page they're on. Additionally, the navigation bar is responsive to different screen sizes and can be collapsed into a 'burger' menu on smaller screens, further enhancing the user experience.

  #### Fig 01-A Desktop example

  < desktop homepage image >

  #### Fig 01-B Mobile example

  < mobile hompage image >

- Fo1 - Authenticated user indicator

The user can affirm when they are authenticated (logged in) after successful
sign up to the site, to which they are taken to the hompage and can view, within
the navbar at the top, a greyed button with their username within it.

#### Fig 02-User Icon upon authentication (signup) to site

< user logged in button icon image >
