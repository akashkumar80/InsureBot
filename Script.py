Branches = [
    {
        "heading": " Initial Greeting",
        "AIResponse": " Hello and very Good Morning Sir, May I speak with {policy_holder_name}?",
        "response": {
            "yes": {
                "AIResponse":"""My name is Veena and I am an Executive calling on behalf of ValuEnable Life Insurance Co. Ltd, this is a service call with regards to your life insurance policy. Is this the right time to speak to you regarding the renewal of your policy?""",
                "response": {
                    "yes": 1,
                    "He/she is busy or can’t talk right now": {
                        "AIResponse": """It will take just 2 minutes of your time. Can we discuss it right now or should I reschedule your call at a better time?""",
                        "response": {
                            "yes": 1,
                            "not a good time to talk now": 2,
                        },
                    },
                    "not a good time to talk now": 2,
                },
            },
            "no": {
                "AIResponse":"May I know your relationship with {policy_holder_name}? ",
                "response": {
                    "Define RelationsShip with Customer": {
                        "AIResponse": """Do you handle {policy_holder_name}'s life insurance policy number {policy_number}? Are you aware of the details of this policy?""",
                        "response": {
                            "yes": 1,
                            "no": 2,
                        }
                    },
                },
            },
            "He/she is busy or can’t talk right now": {
                "AIResponse": """It will take just 2 minutes of your time. Can we discuss it right now or should I reschedule your call at a better time?""",
                "response": {
                    "yes": 1,
                    "no": 2,
                }
            }
        }
    },
    {
        "heading": "Policy Confirmation",
        "AIResponse": """ Let me start by confirming your policy details. Your policy is ValuEnable Life {product_name} insurance policy number is {policy_number}, started on {policy_start_date}, and you've paid {total_premium_paid} so far. The premium of {outstanding_amount} due on {premium_due_date} is still pending, and your policy is currently in “Discontinuance” status, with no life insurance cover. Could you please let me know why you haven’t been able to pay the premium? """,
        "response": {
            "If Customer Explain Reason": {
                "AIResponse": """ I would like to inform you that the due date for renewal premium payment for your policy was on {premium_due_date}, the grace period for your policy is over due to non-payment of the regular premium and you are losing the benefit of your plan. Would you like to know what your policy's benefits you could get if you resume paying premiums?""",
                "response": {
                    "agree/DisAgree": {
                        "AIResponse": """Sir, you will get maximum Allocation in the Invested Fund i. e % of Premium which will boost up your investment. Allocation in renewal premiums is much higher than the initial / first year premium; hence premium payment towards renewals is always monetarily beneficial because of maximum money will be invested into the chosen funds. Addition of Loyalty Units would help to fetch good return in long run and all Renewal premium payments also provide a tax saving benefit under Sec 80(c), 10 (10(D)) as per prevailing provisions of the Indian Income Tax act. Does this help you make a more informed decision about your policy? """,
                        "response": {
                            "agree to pay": 4,
                            "already paid": 5,
                            "don't have policy band": 3,
                            "can't pay": 6,
                            "reason to not pay": 7,
                        },
                    },
                },
            },
            "agree to pay": 4,
            "already paid": 5,
            "don't have policy band": 3,
            "can't pay": 6,
            "reason to not pay": 7,
        }
    },
    {
        "heading": " Arrange call back if customer is busy",
        "AIResponse": """When would be a convenient time to call you again to provide the information about your policy with us? Please can you give a time and date? """,
        "response": {
            "date/Time Provided": {
                "AIResponse": " Thank you sir/maam, I will arrange your call back at the given time.",
                "response": {
                    "instantResponse": 8
                }
            },
        },
    },
    {
        "heading": " Customer doesn’t have policy bond ",
        "AIResponse": """ You can download the policy bond through whatsapp. Please send a message from your registered mobile number on 8806727272 and you will be able to download the policy bond. """,
        "response": {
            "instantResponse": 8
        }
    },
    {
        "heading": "Payment Follow-up",
        "AIResponse": "May I know how you plan to make the payment? Will it be via cash, cheque, or online?",
        "response": {
            "cheque": {
                "AIResponse": """ If you wish, you can pay online now. We’ll send you a link, or you can visit our website. You can use Debit card, Credit card, Net banking, PhonePe, Whatsapp or Google Pay to make the payment.""",
                "response": {
                    "branch": {
                        "AIResponse": """ You can conveniently pay the premium from home without visiting the branch. I’m here to assist you with the digital payment process. """,
                        "response": {
                            "Gives Data": {
                                "AIResponse": """: I’m noting your preference. I’ll send you a payment link for easy processing. """,
                                "response": {
                                    "customer confirms payment details": {
                                        "AIResponse": """ As confirmed, you’ll pay the premium on October 5, 2024, at 10:00 AM via online transfer. Please ensure timely payment to maintain your policy benefits. We’ll call to confirm the payment status.""",
                                        "response": {
                                            "instantResponse": 8,
                                        }
                                    }
                                }
                            }
                        }
                    }

                }
            },
            "branch": {
                "AIResponse": """ You can conveniently pay the premium from home without visiting the branch. I’m here to assist you with the digital payment process. """,
                "response": {
                    "Gives Data": {
                        "AIResponse": """: I’m noting your preference. I’ll send you a payment link for easy processing. """,
                        "response": {
                            "customer confirms payment details ": {
                                "AIResponse": """ As confirmed, you’ll pay the premium on October 5, 2024, at 10:00 AM via online transfer. Please ensure timely payment to maintain your policy benefits. We’ll call to confirm the payment status.""",
                                "response": {
                                    "instantResponse": 8,
                                }
                            }
                        }
                    }
                }
            },
            "Gives Data": {
                "AIResponse": """: I’m noting your preference. I’ll send you a payment link for easy processing. """,
                "response": {
                    "customer confirms payment details ": {
                        "AIResponse": """ As confirmed, you’ll pay the premium on October 5, 2024, at 10:00 AM via online transfer. Please ensure timely payment to maintain your policy benefits. We’ll call to confirm the payment status.""",
                        "response": {
                            "instantResponse": 8,
                        }
                    }
                }
            },
            "customer confirms payment details": {
                "AIResponse": """ As confirmed, you’ll pay the premium on October 5, 2024, at 10:00 AM via online transfer. Please ensure timely payment to maintain your policy benefits. We’ll call to confirm the payment status.""",
                "response": {
                    "instantResponse": 8,
                }
            }
        },
    },
    {
        "heading": "Payment Already Made: ",
        "AIResponse": """ Thank you for making the payment. May I know when you made the payment? """,
        "response": {
            "last week or provide any date": {
                "AIResponse": "May I know where you made the payment (e.g., online, cheque, or cash)?",
                "response": {
                    "online/case/cheque": {
                        "AIResponse": """ Could you please provide the transaction id or reference id? For cheque payments, we’ll need the cheque number. I can assist with further tracking if needed.""",
                        "response": {
                            "instantResponse": 8
                        },
                    },
                    "anything else": 8
                },
            },
            "anything else": 8,
        },
    },
    {
        "heading": " Financial problem: ",
        "AIResponse": """I understand your concern. To achieve your financial goals, staying invested is key. You can pay via credit card, EMI, or change your payment mode to monthly. Can you arrange the premium to continue benefits?""",
        "response": {
            "instantResponse": 8,
        },
    },
    {
        "heading": " Rebuttals:",
        "AIResponse": """You can opt for the Partial Withdrawal option after completing 5 years of the policy i.e ,lock-in period. If premiums stop before the lock-in period ends, the policy will discontinue and growth will be limited to 4-4.5% returns. Also you will lose your sum assured value of {sum_assured}. If you choose to continue with this policy at the time of maturity you will receive {fund_value}. Would you be willing to pay your premium now?""",
        "response": {
            "yes": 2,
            "no": 8,
        },
    },
    {
        "heading": "Conversation Closure: ",
        "AIResponse": """ For any further assistance with your policy, feel free to call our helpline at 1800 209 7272, message us on whatsapp on 8806 727272, mail us or visit our website. Thank you for your valuable time. Have a great day ahead.""",
        "response": {
            "instantResponse": False
        }
    }
]