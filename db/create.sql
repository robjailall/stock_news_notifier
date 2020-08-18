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
    last_update timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    last_diff text
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

