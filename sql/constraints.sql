alter table customers
add primary key (customer_id);

alter table sellers
add primary key (seller_id);

alter table products
add primary key (product_id);

alter table orders
add primary key (order_id);

alter table orders
add constraint fk_customer
foreign key (customer_id)
references customers(customer_id);

alter table order_items
add constraint fk_product
foreign key (product_id)
references products(product_id);

alter table order_items
add constraint fk_seller
foreign key (seller_id)
references sellers(seller_id);

alter table order_items
add constraint fk_order
foreign key (order_id)
references orders(order_id);

alter table order_payments
add constraint fk_payment_order
foreign key (order_id)
references orders(order_id);

alter table order_reviews
add constraint fk_review_order
foreign key (order_id)
references orders(order_id);