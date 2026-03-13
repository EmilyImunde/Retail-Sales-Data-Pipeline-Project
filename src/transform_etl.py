def clean_text(value):
    if value is None:
        return ""
    return value.strip().title()

def clean_customers(customers):
    cleaned_customers = []
    seen_customer_ids = set()

    for customer in customers:
        customer_id = customer.get("customer_id", "").strip()

        if not customer_id:
            continue

        if customer_id in seen_customer_ids:
            continue

        seen_customer_ids.add(customer_id)

        cleaned_customers.append({
            "customer_id": int(customer_id),
            "customer_name": clean_text(customer.get("customer_name")),
            "city": clean_text(customer.get("city")),
            "signup_date": customer.get("signup_date", "").strip()
        })

    return cleaned_customers

