--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: source_crawls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.source_crawls (
    id bigint NOT NULL,
    source_key character varying NOT NULL,
    last_scrape text,
    last_update timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.source_crawls OWNER TO postgres;

--
-- Name: source_crawls_sampleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.source_crawls_sampleid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.source_crawls_sampleid_seq OWNER TO postgres;

--
-- Name: source_crawls_sampleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.source_crawls_sampleid_seq OWNED BY public.source_crawls.id;


--
-- Name: source_crawls id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.source_crawls ALTER COLUMN id SET DEFAULT nextval('public.source_crawls_sampleid_seq'::regclass);


--
-- Data for Name: source_crawls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.source_crawls (id, source_key, last_scrape, last_update) FROM stdin;
1	rob	rob2	2020-08-17 21:37:20.051187
8	treasury_emergency_loans	BorrowerCity2State2Total Anticipated Loan AmountDate of ApplicationDate of Loan Agreement3Transaction Information4YRC WORLDWIDE INC.OVERLAND PARKKS$700,000,0004/29/20207/8/2020Transaction SummaryTransaction Documentation	2020-08-17 21:36:55.516039
9	development_finance_corp_loi	Enter your keywordsSearchSearch helpSearch resultsDFC to Sign Letter of Interest for Investment in Kodak’s Expansion Into PharmaceuticalsDFC to SignLetterofInterestfor Investment in Kodak’s Expansion Into …  Chief Executive Officer Adam Boehler will today sign aletterofinterest(LOI) to provide a $765 million loan to …DFC CEO Adam Boehler Visits Mexico, Signs Letter of Interest to Support Critical Energy Infrastructure in Southern MexicoDFC CEO Adam Boehler Visits Mexico, SignsLetterofInterestto Support Critical Energy Infrastructure in …OPIC Signs Letter of Interest to Invest in Cashew Company in MozambiqueOPIC SignsLetterofInterestto Invest in Cashew Company in Mozambique   \n\n      …  \n\n  OPIC Managing Director for Africa Worku Gachou signed aletterofinterestto finance the project at an event …OPIC CEO Signs Letters of Interest in ArgentinaOPIC CEO Signs LettersofInterestin Argentina  \n\n                November 28, 2018  …  OPIC’s continued commitment to the region.”  \n  \n\n  Theletterofinterestis the first preliminary agreement in the …Defense Production Act (DPA)…  DFC the tools under the DPA to re-shore domestic productionofstrategic resources needed to respond to the COVID-19 …  with the termsofthe loan; and The loan bears a reasonableinterestrate  \n\t  \n\t  Maximum Principal  \n\t  \n\t  Maximum …  an applicant may request, or DFC may wish to send aletterofinterest(LOI). An LOI implies DFC’s willingness …Problem Solving…  problem-solving Consultation may be filed with the OfficeofAccountability by eitherofthe following:  \n\n\t    …  A project is DFC-supported when DFC has clearly indicatedinterestin financing or insuring the project. Such indication is ordinarily provided when a commitmentletteris issued or insurance contract is signed. DFC …Advisor to the President Ivanka Trump and OPIC Acting President and CEO David Bohigian Announce $1 Billion OPIC 2X Africa Women’s Investment Initiative…   Addis Ababa   – David Bohigian, Acting President and CEOofthe Overseas Private Investment Corporation (OPIC), the …   \n\n  Yesterday while in Addis Ababa, Bohigian signed anletterofinterestwith a women owned business called Muya to help …	2020-08-17 21:36:55.516039
\.


--
-- Name: source_crawls_sampleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.source_crawls_sampleid_seq', 16, true);


--
-- Name: source_crawls source_crawls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.source_crawls
    ADD CONSTRAINT source_crawls_pkey PRIMARY KEY (id);


--
-- Name: source_crawls_source_key_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX source_crawls_source_key_idx ON public.source_crawls USING btree (source_key);


--
-- PostgreSQL database dump complete
--

