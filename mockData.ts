export interface Business {
  id: number;
  business_name: string;
  address: string;
  phone: string;
  email: string;
  website: string;
  working_hours: Record<string, string>;
  rating: number;
  review_count: number;
  services: string[];
  license_information: string;
  source_urls: Record<string, string>;
  confidence: "high" | "medium" | "low" | "conflict";
  trust_score: number;
  security_score: number;
  fraud_risk: "Low" | "Medium" | "High";
  verification_count: number;
}

export const MOCK_BUSINESSES: Business[] = [
  {
    id: 1,
    business_name: "Birmingham Heart Clinic",
    address: "100 Pilot Medical Dr, Birmingham, AL 35235",
    phone: "(205) 856-2284",
    email: "info@birminghamheart.com",
    website: "https://birminghamheart.com",
    working_hours: { "Mon-Fri": "8:00 AM - 5:00 PM", "Sat": "9:00 AM - 1:00 PM", "Sun": "Closed" },
    rating: 4.8,
    review_count: 312,
    services: ["Echocardiogram", "Stress Testing", "Cardiac Catheterization", "Pacemaker Implantation"],
    license_information: "AL Medical License #MD-48291",
    source_urls: {
      "Google Business": "https://google.com/maps/place/...",
      "Healthgrades": "https://healthgrades.com/...",
      "Yelp": "https://yelp.com/biz/...",
      "State Board": "https://albme.gov/verify/..."
    },
    confidence: "high",
    trust_score: 94,
    security_score: 100,
    fraud_risk: "Low",
    verification_count: 4
  },
  {
    id: 2,
    business_name: "Cardiology Associates of Birmingham",
    address: "2700 US-280, Birmingham, AL 35223",
    phone: "(205) 871-7745",
    email: "appointments@cardioassoc.com",
    website: "https://cardiologyassociatesbhm.com",
    working_hours: { "Mon-Fri": "7:30 AM - 4:30 PM", "Sat-Sun": "Closed" },
    rating: 4.6,
    review_count: 187,
    services: ["Nuclear Cardiology", "Vascular Surgery", "Heart Failure Management"],
    license_information: "AL Medical License #MD-33104",
    source_urls: {
      "Google Business": "https://google.com/maps/place/...",
      "Vitals": "https://vitals.com/..."
    },
    confidence: "high",
    trust_score: 88,
    security_score: 95,
    fraud_risk: "Low",
    verification_count: 3
  },
  {
    id: 3,
    business_name: "Heart South Cardiovascular Group",
    address: "7191 Cahaba Valley Rd, Birmingham, AL 35242",
    phone: "(205) 599-5600",
    email: "contact@heartsouth.com",
    website: "https://heartsouth.com",
    working_hours: { "Mon-Thu": "8:00 AM - 5:00 PM", "Fri": "8:00 AM - 12:00 PM" },
    rating: 4.5,
    review_count: 156,
    services: ["Interventional Cardiology", "Electrophysiology", "Cardiac Rehab"],
    license_information: "AL Medical License #MD-51822",
    source_urls: {
      "Google Business": "https://google.com/maps/place/...",
      "Healthgrades": "https://healthgrades.com/...",
      "WebMD": "https://webmd.com/..."
    },
    confidence: "high",
    trust_score: 85,
    security_score: 90,
    fraud_risk: "Low",
    verification_count: 3
  },
  {
    id: 4,
    business_name: "UAB Cardiovascular Institute",
    address: "1720 2nd Ave S, Birmingham, AL 35294",
    phone: "(205) 934-4011",
    email: "",
    website: "https://uab.edu/medicine/cardiovascular",
    working_hours: { "Mon-Fri": "8:00 AM - 5:00 PM" },
    rating: 4.7,
    review_count: 523,
    services: ["Heart Transplant", "TAVR", "Complex Coronary Intervention", "Research Trials"],
    license_information: "UAB Hospital System",
    source_urls: {
      "Google Business": "https://google.com/maps/place/...",
      "U.S. News": "https://usnews.com/...",
      "Healthgrades": "https://healthgrades.com/...",
      "UAB Official": "https://uab.edu/..."
    },
    confidence: "medium",
    trust_score: 91,
    security_score: 100,
    fraud_risk: "Low",
    verification_count: 4
  },
  {
    id: 5,
    business_name: "Premier Cardiology Clinic",
    address: "3125 Independence Dr, Birmingham, AL 35209",
    phone: "(205) 802-6100",
    email: "info@premiercardio.com",
    website: "",
    working_hours: {},
    rating: 3.2,
    review_count: 8,
    services: ["General Cardiology"],
    license_information: "",
    source_urls: {
      "Yellow Pages": "https://yellowpages.com/..."
    },
    confidence: "low",
    trust_score: 35,
    security_score: 0,
    fraud_risk: "High",
    verification_count: 1
  },
  {
    id: 6,
    business_name: "Alabama Cardiovascular Group",
    address: "800 Montclair Rd, Birmingham, AL 35213",
    phone: "(205) 592-4100",
    email: "frontdesk@alcardio.com",
    website: "https://alabamacardio.com",
    working_hours: { "Mon-Fri": "8:30 AM - 4:30 PM", "Sat": "By Appointment" },
    rating: 4.1,
    review_count: 94,
    services: ["Preventive Cardiology", "Lipid Management", "Arrhythmia Treatment"],
    license_information: "AL Medical License #MD-45019",
    source_urls: {
      "Google Business": "https://google.com/maps/place/...",
      "Yelp": "https://yelp.com/biz/..."
    },
    confidence: "conflict",
    trust_score: 62,
    security_score: 75,
    fraud_risk: "Medium",
    verification_count: 2
  }
];
