from silentauction.utils.date_utils import now_plus_days_datetime

# Auction Descriptions
acs_desc = "The American Cancer Society (ACS) stands as a prominent organization dedicated to the fight against cancer. Founded in 1913 by a group of 15 healthcare professionals and business leaders, the ACS has evolved into a comprehensive force in cancer research, education, advocacy, and patient support. With a mission to eliminate cancer as a major health problem, the organization channels its efforts into groundbreaking research initiatives, striving to discover new treatments and enhance existing ones.\nThe ACS plays a pivotal role in educating the public about cancer prevention, early detection, and the importance of a healthy lifestyle. Through various campaigns, resources, and community outreach programs, the organization empowers individuals with knowledge to make informed decisions about their health. Additionally, the ACS advocates for evidence-based policies to address the broader societal impact of cancer, influencing legislation and fostering a supportive environment for those affected by the disease.\nCommitted to supporting cancer patients and their families, the ACS offers a range of services, including patient transportation to treatment, lodging assistance, and emotional support programs. The organization's Relay For Life events, held nationwide, bring communities together to celebrate survivors, remember loved ones lost, and raise funds for continued research and support services.\nIn summary, the American Cancer Society stands as a beacon of hope in the fight against cancer, leveraging research, education, advocacy, and compassionate support to make strides towards a world free from the burden of this pervasive disease."
fa_desc = "Feeding America is a prominent nonprofit organization dedicated to alleviating hunger and food insecurity in the United States. Established in 1979, the organization operates as a nationwide network of food banks and pantries, collaborating with various community-based agencies to distribute meals to those in need. The overarching mission of Feeding America is to combat hunger and ensure that every individual in the country has access to nutritious food.\nThe organization's impact is vast, as it serves millions of Americans annually, including children, seniors, and families facing economic challenges. Feeding America operates strategically, harnessing partnerships with food manufacturers, retailers, and volunteers to secure and distribute billions of pounds of food each year.\nOne notable initiative spearheaded by Feeding America is its focus on addressing food waste. By rescuing surplus food that would otherwise go to waste and redirecting it to those experiencing hunger, the organization contributes to both hunger relief and environmental sustainability.\nIn addition to its emergency food distribution efforts, Feeding America engages in advocacy to address the root causes of hunger, promoting policies and programs that strive to create a hunger-free America. Through its multifaceted approach, Feeding America remains a vital force in the fight against hunger, striving to create a future where every individual has consistent access to nutritious meals and the resources needed to thrive"
uww_desc = "United Way Worldwide is a renowned international charitable organization dedicated to addressing pressing social issues and improving communities around the globe. Founded in 1887, the organization has grown into a vast network of local United Way chapters in nearly 40 countries and territories. United Way Worldwide focuses on collaborative community impact, bringing together governments, businesses, nonprofit organizations, and individuals to create lasting solutions to societal challenges.\nOne of the distinctive features of United Way is its emphasis on community-based solutions tailored to the unique needs of each locality. By conducting extensive research and needs assessments, United Way identifies key issues affecting communities, such as education, health, and financial stability, and works strategically to address them. The organization leverages partnerships and volunteer engagement to maximize its impact, emphasizing the collective power of individuals coming together for the greater good.\nUnited Way's fundraising efforts support a wide range of initiatives, from early childhood education programs to emergency relief efforts during natural disasters. The organization's commitment to transparency and accountability ensures that donor contributions are utilized efficiently and effectively to drive positive change. With a vision of creating a world where every person has the opportunity to live a fulfilling life, United Way Worldwide continues to inspire collaboration and philanthropy on a global scale."

# Auction Item Descriptions
vase_desc = "The centerpiece of the upcoming auction is an exquisite vase that captures the essence of timeless elegance and artistic craftsmanship. This remarkable piece, poised to allure discerning collectors and enthusiasts alike, stands as a testament to the mastery of its creator. Crafted with meticulous precision, the vase seamlessly blends classical aesthetics with contemporary sensibilities, making it a rare gem in the realm of decorative art. Fashioned from the finest porcelain, the vase boasts a delicate yet durable form that gracefully curves upward, creating a silhouette reminiscent of classical Grecian urns. Its surface is adorned with intricate hand-painted patterns, each stroke revealing the artisan's dedication to detail. The color palette, a harmonious fusion of soft pastels and rich metallic accents, enhances the vase's allure, adding depth and sophistication to its overall appearance. What sets this vase apart is its unique blend of tradition and innovation. While its design pays homage to historical art movements, the vase incorporates modern elements, making it a versatile and captivating addition to any collection. The artist's signature, discreetly inscribed on the base, further adds to the provenance and exclusivity of this exceptional piece."
jc_letter_desc = "This framed photograph features a beloved comedy icon and is a must-have for any fan of the movie 'Nothing But Trouble.' The signature of John Candy, who starred in the film, adds a unique touch to this original piece of entertainment memorabilia. The photograph is in excellent condition and would make a great addition to any collection of autographs or photographs. Don't miss out on the opportunity to own this one-of-a-kind item."

seeds_config = {
    "users": [
        {
            "ref_id": "user1",
            "first_name": "Steve",
            "last_name": "Wisner",
            "email": "steve@test.com",
            "username": "steve987",
            "password": "test1234!"
        },
        {
            "ref_id": "user2",
            "first_name": "Ned",
            "last_name": "Chase",
            "email": "ned@test.com",
            "username": "ned1234",
            "password": "test1234!"
        }
    ],
    "auctions": [
        {
            "ref_id": "auction1",
            "name": "American Cancer Society",
            "category": "Health",
            "description": acs_desc,
            "auction_items": [
                {
                    "ref_id": "item1",
                    "name": "Vase",
                    "description": vase_desc,
                    "starting_bid": 10.00,
                    "bid_interval": 5.00,
                    "auction_start": None,
                    "auction_end": None,
                    "photos": [
                        {
                            "filename": "auction-item-photos/vase/vase-1.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        },
                    ]
                },
                {
                    "ref_id": "item2",
                    "name": "Signed Liverpool FC Jersey",
                    "description": "This signed Liverpool FC jersey is a must-have for any fan of the team. The jersey is in excellent condition and features the signature of Virgil Van Dyke. Don't miss out on the opportunity to own this unique piece of sports memorabilia.",
                    "starting_bid": 99.00,
                    "bid_interval": 10.00,
                    "auction_start": now_plus_days_datetime(days=1, hours=2, seconds=35, minutes=15),
                    "auction_end": now_plus_days_datetime(days=45, hours=8, seconds=10, minutes=45),
                    "photos": [
                        {
                            "filename": "auction-item-photos/lfc-signed-jersey/lfc-signed-1.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        },
                    ]
                },
                {
                    "ref_id": "item3",
                    "name": "Red Sox Tickets",
                    "description": "This pair of Red Sox tickets is a great opportunity to see the team in action at Fenway Park. The tickets are for a game against the New York Yankees and are located in the grandstand section. Don't miss out on the chance to experience the excitement of a Red Sox game from the stands.",
                    "starting_bid": 99.00,
                    "bid_interval": 10.00,
                    "auction_end": now_plus_days_datetime(days=0, hours=0, seconds=0, minutes=1),
                    "photos": [
                        {
                            "filename": "auction-item-photos/red-sox-tickets/red-sox-tickets-1.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        },
                    ]
                }
            ]
        },
        {
            "ref_id": "auction2",
            "name": "Feeding America",
            "category": "Domestic Needs",
            "description": fa_desc,
            "auction_items": [
                {
                    "ref_id": "item4",
                    "name": "John Candy Signed Letter from Warner Brothers",
                    "description": jc_letter_desc,
                    "starting_bid": 149.99,
                    "bid_interval": 15.00,
                    "auction_start": None,
                    "auction_end": None,
                    "photos": [
                        {
                            "filename": "auction-item-photos/john-candy-signed-letter/jc-1.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        },
                        {
                            "filename": "auction-item-photos/john-candy-signed-letter/jc-2.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        },
                        {
                            "filename": "auction-item-photos/john-candy-signed-letter/jc-3.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        },
                        {
                            "filename": "auction-item-photos/john-candy-signed-letter/jc-4.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        },
                        {
                            "filename": "auction-item-photos/john-candy-signed-letter/jc-5.png",
                            "category": "AUCTION_ITEM", 
                            "subcategory": "ITEM_PHOTO"
                        }
                    ]
                }
            ]
        },
        {
            "ref_id": "auction3",
            "name": "United Way Worldwide",
            "category": "Domestic Needs",
            "description": uww_desc,
            "auction_items":[]
        },
    ],
}

def get_seed_config():
    return seeds_config