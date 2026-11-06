
# AIMS-mini – Use Cases

## Actor

Customer – Người sử dụng ứng dụng AIMS-mini.

## Use Case 1: Add DVD to Cart

**Description:** Customer adds a DVD to the shopping cart.

**Precondition:** The DVD is available.

**Main Flow:**
1. Customer selects a DVD.
2. System checks cart capacity.
3. System adds the DVD to the cart.
4. System displays a success message.

**Alternative Flow:**
- If the cart is full, the system rejects the DVD.

## Use Case 2: Remove DVD from Cart

**Description:** Customer removes a DVD from the shopping cart.

**Main Flow:**
1. Customer selects a DVD to remove.
2. System checks whether the DVD exists in the cart.
3. System removes the DVD.
4. System displays a confirmation message.

## Use Case 3: View Cart

**Description:** Customer views all DVDs in the cart.

**Main Flow:**
1. Customer requests to view the cart.
2. System displays the DVD list.
3. System displays the total cost.

**Alternative Flow:**
- If the cart is empty, the system displays "The cart is empty".

## Use Case 4: Search DVD by Title

**Description:** Customer searches for DVDs using a title keyword.

**Main Flow:**
1. Customer enters a keyword.
2. System searches DVD titles.
3. System returns matching DVDs.

**Alternative Flow:**
- If no DVD matches, the system returns an empty list.

## Use Case 5: Calculate Total Cost

**Description:** System calculates the total cost of all DVDs in the cart.

**Main Flow:**
1. System retrieves DVDs in the cart.
2. System sums their prices.
3. System returns the total cost.
