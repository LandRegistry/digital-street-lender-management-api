
INSERT INTO "restriction" (restriction_id, restriction_type, restriction_text)
VALUES	('BX102', 'CBCR', 'RESTRICTION: No disposition of the registered estate by the proprietor of the registered estate is to be registered without a written consent signed by the proprietor for the time being of the Charge dated *CD* in favour of *CP* referred to in the Charges Register.'),
		('BX750', 'ORES', 'RESTRICTION: No disposition by the proprietor of the registered estate to which section 36 or section 38 of the Charities Act 1993 applies is to be registered unless the instrument contains a certificate complying with section 37(2) or section 39(2) of that Act as appropriate.');


INSERT INTO "address" (address_id, house_name_number, street, town_city, county, country, postcode)
VALUES	(1, '1', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN'),

		(2, '10', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN'),
		(3, '11', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN'),

		(4, '20', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN'),
		(5, '21', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN'),

		(6, '30', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN'),
		(7, '31', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN'),
		(8, '32', 'Digital Street', 'Bristol', 'Bristol', 'England', 'BS2 8EN');
ALTER SEQUENCE "address_address_id_seq" RESTART WITH 9;

INSERT INTO "user" (identity, first_name, last_name, email_address, phone_number, address_id)
VALUES	(1, 'Lisa', 'White', 'lisa.white@example.com', '07700900354', 2),
		(2, 'David', 'Jones', 'david.jones@example.com', '07700900827', 3),

		(3, 'Natasha', 'Powell', 'natasha.powell@example.com', '07700900027', 4),
		(4, 'Samuel', 'Barnes', 'samuel.barnes@example.com', '07700900534', 5),

		(5, 'Jim', 'Smith', 'jim.smith@example.com', '07700900815', 6),
		(6, 'Martin', 'Keats', 'martin.keats@example.com', '07700900133', 7),
		(7, 'Holly', 'Windsor', 'holly.windsor@example.com', '07700900970', 8);
