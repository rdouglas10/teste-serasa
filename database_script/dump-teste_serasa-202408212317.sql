--
-- PostgreSQL database dump
--

-- Dumped from database version 12.20 (Ubuntu 12.20-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.20 (Ubuntu 12.20-0ubuntu0.20.04.1)

-- Started on 2024-08-21 23:17:44 -03

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

DROP DATABASE teste_serasa;
--
-- TOC entry 2973 (class 1262 OID 41208)
-- Name: teste_serasa; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE teste_serasa WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'pt_BR.UTF-8' LC_CTYPE = 'pt_BR.UTF-8';


ALTER DATABASE teste_serasa OWNER TO postgres;

\connect teste_serasa

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

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 2974 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 41407)
-- Name: produtor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produtor (
    id integer NOT NULL,
    cpf_cnpj character varying(18) NOT NULL,
    nome_produtor character varying(100) NOT NULL,
    nome_fazenda character varying(100) NOT NULL,
    cidade character varying(50) NOT NULL,
    estado character varying(2) NOT NULL,
    area_total double precision NOT NULL,
    area_agricultavel double precision NOT NULL,
    area_vegetacao double precision NOT NULL,
    culturas character varying NOT NULL
);


ALTER TABLE public.produtor OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 41405)
-- Name: produtor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produtor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.produtor_id_seq OWNER TO postgres;

--
-- TOC entry 2975 (class 0 OID 0)
-- Dependencies: 202
-- Name: produtor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produtor_id_seq OWNED BY public.produtor.id;


--
-- TOC entry 2835 (class 2604 OID 41410)
-- Name: produtor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtor ALTER COLUMN id SET DEFAULT nextval('public.produtor_id_seq'::regclass);


--
-- TOC entry 2967 (class 0 OID 41407)
-- Dependencies: 203
-- Data for Name: produtor; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.produtor VALUES (1, '96448566000150', 'Anastácio Nascimento', 'Fazenda mato alto', 'Maceió', 'AL', 90000, 50000, 30000, 'Milho');
INSERT INTO public.produtor VALUES (3, '96448566000150', 'Anastácio Nascimento', 'Fazenda mato baixo', 'Maceió', 'AL', 90000, 50000, 30000, 'Milho');
INSERT INTO public.produtor VALUES (4, '01201753000128', 'Florência Diniz', 'Fazenda sapo boi', 'Maceió', 'AL', 90000, 50000, 30000, 'Soja');


--
-- TOC entry 2976 (class 0 OID 0)
-- Dependencies: 202
-- Name: produtor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produtor_id_seq', 4, true);


--
-- TOC entry 2837 (class 2606 OID 41417)
-- Name: produtor produtor_nome_fazenda_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtor
    ADD CONSTRAINT produtor_nome_fazenda_key UNIQUE (nome_fazenda);


--
-- TOC entry 2839 (class 2606 OID 41415)
-- Name: produtor produtor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtor
    ADD CONSTRAINT produtor_pkey PRIMARY KEY (id);


-- Completed on 2024-08-21 23:17:44 -03

--
-- PostgreSQL database dump complete
--

