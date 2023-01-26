# Testing
Throughout the entire development, testing was ongoing. Throughout the development process, I used Google's Developer Tools to check that everything was operating as expected and and carried out debugging when necessary. I used both manual testing and automated testing using unit test. Majority of the website is validated with automated testing. Due to time constraints only small portion of the site was not tested with automated testing.
### Table of contents
- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)

    - [User Story](#user-story)
        
        - [As a User](#as-a-user)
        - [As a Store Owner](#as-a-store-owner)

- [Validator Testing](#validator-testing)

    - [HTML](#html)
    - [CSS](#css)
    - [JS](#js)
    - [PYTHON](#python)
    - [LIGHTHOUSE ](#lighthouse)

## Automated Testing


## Manual Testing
### User Story

### As a User


- I can rapidly grasp what the website is presenting so that I can determine whether it satisfies my needs.

    - The front page of the website gives the user information about the content of the website.
- I can sign up for a monthly newsletter
    - A newsletter sign up form is provided on the footer of every page.
- I can browse frequently asked questions
    - Every page of the website has a footer with a link to the FAQ page
- I can fill in a contact form if I needed to contact the store owner
    - A form is provided in the contact page which is located at the bottom of the page.

**User Story:**

### As a site I can view the products on the home page so that I can easily browse them [#1](https://github.com/shahid129/oliver-dein/issues/1)

**Acceptance Criteria:**
- A list of products is available on the home page

**Expected Results**
- A list of Featured  products should be displayed on the page [Image](docs/screenshot/testing/featured-product.png)
- A list of recently added products should be displayed on the page [Image](docs/screenshot/testing/recently-product.png)

**Actual Results**
- A list of recently added products is displayed on the page [Image](docs/screenshot/testing/featured-product.png)
- A list of recently added products is displayed on the page [Image](docs/screenshot/testing/recently-product.png)

**Results: Pass**


### As a site user I can see the featured products so that I know which items are featured [#2](https://github.com/shahid129/oliver-dein/issues/2)

**Acceptance Criteria:**
- Users can view the featured products on the home page

**Expected Results**
- A list of Featured  products should be displayed on the page [Image](docs/screenshot/testing/featured-product.png)

**Actual Results**
- A list of recently added products is displayed on the page [Image](docs/screenshot/testing/featured-product.png)

**Results: Pass**


### As a site user I can see the menu all the time so that I don't have to scroll all the way up [#3](https://github.com/shahid129/oliver-dein/issues/3)

**Acceptance Criteria:**
- The navigation menu must be user-friendly and stays on top of the page

**Expected Results**
- The drop down menu opens up on hover, so that users do not need to click on it
- The menu stays on top all the time [Image](docs/screenshot/testing/menu.png)

**Actual Results**
- The drop down menu opens up on hover, so that users do not need to click on it
- The menu stays on top all the time [Image](docs/screenshot/testing/menu.png)

**Results: Pass**


### As a site user I can search products so that I can find them easily [#4](https://github.com/shahid129/oliver-dein/issues/4)

**Acceptance Criteria:**
- User can search for products
- User can click on the searched products to view the products

**Expected Results**
- The search bar is located on the nav menu and user have access to search on all pages all time
- Search an item, and if the search is successful, it will display the product, and you can view the product.
- If no item is found, it will tell you '0 Products Found' [Image](docs/screenshot/testing/search.png)
- IT will also show you number of products found

**Actual Results**
- The searched item is displayed on the page if the item is found [Image](docs/screenshot/testing/search.png)
- If no item is found, it will tell you '0 Products Found' 
- It shows the number of products found

**Results: Pass**

### As a site user I can sort out products so that I can view them in different ways [#5](https://github.com/shahid129/oliver-dein/issues/5)

**Acceptance Criteria:**
- User can sort out the products

**Expected Results**
- Click on the sort out button
- It will display a drop-down menu with different ways of sorting [Image](docs/screenshot/testing/sort.png)
- Click on any of the drop-down menus, and the products will be sorted accordingly.

**Actual Results**
- The products are sorted accordingly when clicked on it [Image](docs/screenshot/testing/sort.png)

**Results: Pass**

### As a site user I can **see review of each products ** so that I know the opinion of other people [#6](https://github.com/shahid129/oliver-dein/issues/6)

**Acceptance Criteria:**
- As a site user I can see review of each products so that I know the opinion of other people

**Expected Results**
- The user can see reviews of a product related to a product if a review exists.
- User can create a review for a product [Image](docs/screenshot/testing/review.png)
- User can also see review in the home page in a carousel [Image](docs/screenshot/testing/review-carosel.png)

**Actual Results**
- The user can see reviews of a product related to a product if a review exists.
- User can create a review for a product [Image](docs/screenshot/testing/review.png)
- User can also see review in the home page in a carousel [Image](docs/screenshot/testing/review-carosel.png)

**Results: Pass**

### As a site user I can change the quantity so that I can add the required number of items in the bag [#7](https://github.com/shahid129/oliver-dein/issues/7)

**Acceptance Criteria:**
- User can change the quantity of the products
- The +/- button will disable at 1 and 100,

**Expected Results**
- Navigate to any product detail page and you will see a +/- button
- Click on the +/- button to change the quantity of the items [Image](docs/screenshot/testing/%2B%3A-button.png)
- Click "Add to Bag" to add the product to the bag [Image](docs/screenshot/testing/%2B%3A-button.png)

**Actual Results**
- The +/- button changes the quantity of the products

**Results: Pass**

### As a site user I can get notified so that i know every steps i am taking before buying products [#8](https://github.com/shahid129/oliver-dein/issues/8)

**Acceptance Criteria:**
- Users should know what they are doing by giving them visual interactions

**Expected Results**
- The user should get notified of all the actions they take on the page
- sign in, sign out, add to basket, email notification etc

**Actual Results**
- The user is notified about their interaction

**Results: Pass**

### As a site user I can adjust shopping bag quantity so that I don not have to go back to products to adjust my bag [#9](https://github.com/shahid129/oliver-dein/issues/9)

**Acceptance Criteria:**
- User can change the quantity of the products
- The +/- button will be disable at 1 and 100,

**Expected Results**
- Navigate to the shopping bag page and you will see a +/- button
- Click on the +/- button to change the quantity of the items [Image](docs/screenshot/testing/%2B%3A-button.png)
- Click "Add to Bag" to add the product to the bag [Image](docs/screenshot/testing/%2B%3A-button.png)
- The +/- button is disabled at 1 and 100,

**Actual Results**
- The +/- button changes the quantity of the products
- The +/- button is disabled at 1 and 100,

**Results: Pass**

### As a site user I can get email confirmation about my order so that I have all the details of my order [#11](https://github.com/shahid129/oliver-dein/issues/11)

**Acceptance Criteria:**
- Users can view their order details after they completed the order
- Users need to receive an email with the order confirmation

**Expected Results**
- Navigate to the shopping bag page and complete an order
- You will see checkout success page with your order details [Image](docs/screenshot/testing/order-confirmation.png)
- You will also receive an email with your order details [Image](docs/screenshot/testing/order-confirmation-email.png)

**Actual Results**
- Checkout success page loads with order details [Image](docs/screenshot/testing/order-confirmation.png)
- An email is sent with order details [Image](docs/screenshot/testing/order-confirmation-email.png)

**Results: Pass**

### As a user I can see the number of items in shopping bag so that I can keep track of what I am purchasing [#12](https://github.com/shahid129/oliver-dein/issues/12)

**Acceptance Criteria:**
- Users can see the number of each product in the bag
- Users can update the number of products from the bag

**Expected Results**
- Navigate to the shopping bag page and you will see a +/- button
- The number of items in the bag is displayed between the + and - buttons [Image](docs/screenshot/testing/%2B%3A-button.png)

**Actual Results**
- The number of items in the bag is displayed between the + and - buttons [Image](docs/screenshot/testing/%2B%3A-button.png)

**Results: Pass**


### As a site user I can see the price of individual items so that I know how much I am spending on each item [#13](https://github.com/shahid129/oliver-dein/issues/13)

**Acceptance Criteria:**
- Users can see the number of each product in the bag and their individual price
- Users can see the subtotal of a product as well

**Expected Results**
- Navigate to the shopping bag page and you will see a +/- button
- The number of items in the bag is displayed between the + and - buttons [Image](docs/screenshot/testing/%2B%3A-button.png)
- The individual price of each item is displayed on the right side
- Subtotal is displayed at the far end [Image](docs/screenshot/testing/shopping-bag-each-price.png)

**Actual Results**
- The individual price of each item is displayed on the right side
- Subtotal is displayed at the far end [Image](docs/screenshot/testing/shopping-bag-each-price.png)

**Results: Pass**


### As a site user I can see the total cost so that I can track my total purchasing amount [#14](https://github.com/shahid129/oliver-dein/issues/14)

**Acceptance Criteria:**
- Users can see the total price of the products

**Expected Results**
- Add some products to the shopping bag and navigate to the shopping bag
- The total price of the items in the bag is shown at the bottom, right hand side [Image](docs/screenshot/testing/shopping-bag-grand-total.png)

**Actual Results**
- The total price of the items in the bag is shown at the bottom, right hand side [Image](docs/screenshot/testing/shopping-bag-grand-total.png)

**Results: Pass**


### Orders and Checkout - Delivery info [#15](https://github.com/shahid129/oliver-dein/issues/15)

**Acceptance Criteria:**
- As a site user I can enter my delivery and shipping info so that I can checkout quickly and easily

**Expected Results**
- Add a product and go to the shopping bag and go to checkout page
- Enter your details to purchase the product [Image](docs/screenshot/testing/delivery-info.png)
- No need to sign up to purchase item unless you want to save your details for future

**Actual Results**
- The Users can fill up the delivery information form [Image](docs/screenshot/testing/delivery-info.png)
- The users can purchase products without needing to create an account

**Results: Pass**


### Orders and Checkout - Delete Shopping bag items [#16](https://github.com/shahid129/oliver-dein/issues/16)

**Acceptance Criteria:**

-  As a site user I can get a notification if i want to delete items from bag so that I can rectify my mistake if I pressed the delete button unintentionally 

**Expected Results**
- Add a product and go to the shopping bag
- Click on delete product
- Notify users if they really want to delete the product [Image](docs/screenshot/testing/remove-bag.png)
- On final confirmation delete the product [Image](docs/screenshot/testing/remove-bag-notification.png)

**Actual Results**
- Notify users if they really want to delete the product [Image](docs/screenshot/testing/remove-bag.png)
- On final confirmation delete the product [Image](docs/screenshot/testing/remove-bag-notification.png)

**Results: Pass**

### Orders and Checkout - Delivery cost [#17](https://github.com/shahid129/oliver-dein/issues/17)

**Acceptance Criteria:**
- As a site user I can see the delivery cost so that I know how much I am paying for delivery 

**Expected Results**
- Add a product to the basket that is less than €30, and you will be notified how much you need to spend more to get free delivery.
- When you go the bag page, you can see the delivery cost for the purchase [Image](docs/screenshot/testing/free-delivery.png)

**Actual Results**
- Add a product to the basket that is less than €30, and you will be notified how much you need to spend more to get free delivery.
- When you go the bag page, you can see the delivery cost for the purchase [Image](docs/screenshot/testing/free-delivery.png)

**Results: Pass**


### As a site user I can register and login to my account so that I can store my details securely [#25](https://github.com/shahid129/oliver-dein/issues/25)

**Acceptance Criteria:**
- User needs to receive a confirmation email on registration
- Once the email is confirmed user can log in to the site [Image](docs/screenshot/testing/sign-in.png)
- Notify a user about login and account creation

**Expected Results**
- Once you have registered for an account, you will be sent an email
- Once the email confirmed you can log in page where you can login to the site  Image](docs/screenshot/testing/sign-in.png)

**Actual Results**
- Use is able to sign in to the site from the sign in page

**Results: Pass**

### As a site user I can get email confirmation so that I know that my email id is correct [#26](https://github.com/shahid129/oliver-dein/issues/26)

**Acceptance Criteria:**
- User needs to receive a confirmation email on registration
- Once the email is confirmed user can log in to the site
- Notify a user about login and account creation

**Expected Results**
- Click on Account and then Register button from the menu
- Fill out the form and hit sign up
- You will receive an email with a link to verify your email [Image](docs/screenshot/testing/register-email.png)
- Click on the link in the email 
- You will be brought back to the site to confirm again
- Once confirmed you will be redirected to log in page

**Actual Results**
- Click on Account and then Register button from the menu
- Fill out the form and hit sign up
- You will receive an email with a link to verify your email [Image](docs/screenshot/testing/register-email.png)
- Click on the link in the email 
- You will be brought back to the site to confirm again
- Once confirmed you will be redirected to log in page

**Results: Pass**


### As a site user I can login so that I can keep track of my purchases and store my details securely [#27](https://github.com/shahid129/oliver-dein/issues/27)

**Acceptance Criteria:**
- Notify a user about login to the site
- Give users the option to save their details for the next purchase

**Expected Results**
-  Click on the Sign In button from the menu
-  If you already have your account, fill up the form and click Sign In.
-  You will be redirected to home page
-  A pop up appears saying that 'You are logged in as NAME' [Image](docs/screenshot/testing/signin.png)
-  In checkout page page you can save your details for future purchases [Image](docs/screenshot/testing/save_deli_info.png)

**Actual Results**
-  Click on the Sign In button from the menu
-  If you already have your account, fill up the form and click Sign In.
-  You will be redirected to home page
-  A pop up appears saying that 'You are logged in as NAME'
-  In checkout page page you can save your details for future purchases

**Results: Pass**

### As a site I can logout so that my account remains safe [#28](https://github.com/shahid129/oliver-dein/issues/28)

**Acceptance Criteria:**
- Notify a user about log out from the site

**Expected Results**
- Click on the Sign Out button from the menu
- It will ask you if you really want to sign out
- A pop up appears saying that 'You have signed out' [Image](docs/screenshot/testing/sign-out.png)
- You will be redirected to home page

**Actual Results**
- Click on the Sign Out button from the menu
- It will ask you if you really want to sign out
- A pop up appears saying that 'You have signed out'
- You will be redirected to home page

**Results: Pass**


### As a Store Owner

### As a admin I can add products from the site so that I do not have to log in to the admin site [#18](https://github.com/shahid129/oliver-dein/issues/18)

**Acceptance Criteria:**
- Store owners can add products

**Expected Results**
- Log in to the site with your admin details
- Go to stock management under the account section in the menu
- Here, you can add a product [Image](docs/screenshot/testing/product-management.png)

**Actual Results**
- Store owners or admin can add a products without logging into the admin site [Image](docs/screenshot/testing/product-management.png)

**Results: Pass**

### As a admin I can edit an item so that I can edit and update the items easily [#19](https://github.com/shahid129/oliver-dein/issues/19)

**Acceptance Criteria:**
- Store owners can edit products

**Expected Results**
- Log in to the site with your admin details
- Go to any product you wish to edit
- Click on the edit button which is only vissible to admin or superuser
- Here, you can edit a product [Image](docs/screenshot/testing/product-management-edit.png)

**Actual Results**
- Store owners or admin can edit a products without logging into the admin site [Image](docs/screenshot/testing/product-management-edit.png)

**Results: Pass**


### As a admin I can delete item so that I can move it from website [#20](https://github.com/shahid129/oliver-dein/issues/20)

**Acceptance Criteria:**
- Store owners can delete products

**Expected Results**
- Log in to the site with your admin details
- Go to any product you wish to delete
- Click on the delete button which is only vissible to admin or superuser
- Here, you can delete a product [Image](docs/screenshot/testing/product-management-delete.png)
- You will be asked to confirm if you really want to delete the product

**Actual Results**
- Store owners or admin can edit a products without logging into the admin site [Image](docs/screenshot/testing/product-management-delete.png)

**Results: Pass**

### As a Admin I can add faqs so that I can faqs easily to the page [#21](https://github.com/shahid129/oliver-dein/issues/21)

**Acceptance Criteria:**
- Store owners can add faqs

**Expected Results**
- Log in to the site with your admin details
- Go to FAQS at the bottom of the page
- Click on ADD FAQS to add new faqs
- Here, you add FAQS [Image](docs/screenshot/testing/faqs-add.png)


**Actual Results**
- Store owners or admin can add faqs without logging into the admin site [Image](docs/screenshot/testing/faqs-add.png)

**Results: Pass**


### As a Admin I can add faqs so that I can faqs easily to the page [#21](https://github.com/shahid129/oliver-dein/issues/21)

**Acceptance Criteria:**
- Store owners can edit faqs

**Expected Results**
- Log in to the site with your admin details
- Go to FAQS at the bottom of the page
- Click on EDIT FAQS to add 
- Here, you edit FAQS [Image](docs/screenshot/testing/faqs-edit.png)


**Actual Results**
- Store owners or admin can edit faqs without logging into the admin site [Image](docs/screenshot/testing/faqs-edit.png)

**Results: Pass**


### As an admin I can delete faqs so that I can remove from the page [#23](https://github.com/shahid129/oliver-dein/issues/23)

**Acceptance Criteria:**
- Store owners can delete faqs

**Expected Results**
- Log in to the site with your admin details
- Go to FAQS at the bottom of the page
- Click on Delete FAQS to add 
- Here, you edit FAQS [Image](docs/screenshot/testing/faqs-delete.png)


**Actual Results**
- Store owners or admin can edit faqs without logging into the admin site [Image](docs/screenshot/testing/faqs-delete.png)

**Results: Pass**


### As a Admin I can approve or delete comments so that I can keep my website safe and clean place inappropriate words [#24](https://github.com/shahid129/oliver-dein/issues/24)

**Acceptance Criteria:**
- Only the admin can approve or delete comments

**Expected Results**
- Log in to the admin-site with your admin details
- Go to Comment section from the menu on the left hand side
- Click on the comment that you want to approve or delete [Image](docs/screenshot/testing/comment-review.png)



**Actual Results**
- Store owners or admin can approve or delete comments [Image](docs/screenshot/testing/comment-review.png)


**Results: Pass**


### Validator Testing


### HTML
Page Title | Result | Evidence | 
--- | --- | --- |
Home | Pass | [Home Page Validation](docs/screenshot/testing/validation-home.png)
Products | Pass | [Products Page Validation](docs/screenshot/testing/validation-products.png)
Products Detail | Pass | [Products Detail Page Validation](docs/screenshot/testing/validation-product-detail.png)
Privacy | Pass | [Privacy Page Validation](docs/screenshot/testing/validation-privacy.png)
Contact | Pass | [Contact Page Validation](docs/screenshot/testing/validation-contact.png)
Sign Up | Pass | [Sign Up Page Validation](docs/screenshot/testing/validation-signup.png)
Sign In | Pass | [Sign In Page Validation](docs/screenshot/testing/validation-sign-in.png)
Bag | Pass | [bag Page Validation](docs/screenshot/testing/validation-bag.png)
