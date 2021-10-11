--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)

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
-- Name: fruit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.fruit (
    idf integer NOT NULL,
    fruit character varying(60) NOT NULL,
    price integer DEFAULT 10 NOT NULL
);


--
-- Name: history; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.history (
    nno integer NOT NULL,
    username character varying(60) NOT NULL,
    purchase character varying(1000) NOT NULL,
    change character varying(60) NOT NULL,
    date_time character varying(1000) DEFAULT '15:18:08 30-08-2021'::character varying NOT NULL
);


--
-- Name: history_nno_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.history_nno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: history_nno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.history_nno_seq OWNED BY public.history.nno;


--
-- Name: historymoney; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.historymoney (
    nno bigint NOT NULL,
    username character varying(60) NOT NULL,
    money_add character varying(100) NOT NULL,
    date_time character varying(100) NOT NULL
);


--
-- Name: historymoney_nno_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.historymoney_nno_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: historymoney_nno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.historymoney_nno_seq OWNED BY public.historymoney.nno;


--
-- Name: infor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.infor (
    username character varying(60) NOT NULL,
    password character varying(60) NOT NULL,
    email character varying(60),
    ip character varying(60) NOT NULL,
    id bigint NOT NULL
);


--
-- Name: infor_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.infor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: infor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.infor_id_seq OWNED BY public.infor.id;


--
-- Name: onfor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.onfor (
    ip character varying(60) NOT NULL,
    realname character varying(60) NOT NULL,
    phone character varying(60),
    id integer NOT NULL
);


--
-- Name: salary; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.salary (
    rank character varying(60) NOT NULL,
    timework character varying(60),
    salary integer,
    ids integer DEFAULT 1 NOT NULL
);


--
-- Name: history nno; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.history ALTER COLUMN nno SET DEFAULT nextval('public.history_nno_seq'::regclass);


--
-- Name: historymoney nno; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historymoney ALTER COLUMN nno SET DEFAULT nextval('public.historymoney_nno_seq'::regclass);


--
-- Name: infor id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.infor ALTER COLUMN id SET DEFAULT nextval('public.infor_id_seq'::regclass);


--
-- Data for Name: fruit; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.fruit (idf, fruit, price) FROM stdin;
1	cam	10
2	xoai	20
3	tao	30
4	vai	40
\.


--
-- Data for Name: history; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.history (nno, username, purchase, change, date_time) FROM stdin;
96	saler4	'xoai:1', 'cam:1', 'tao:1'	3852	09:06:50 22-09-2021
97	saler4	'xoai:1', 'cam:1', 'tao:1'	3792	09:06:52 22-09-2021
98	saler4	'xoai:1', 'cam:1', 'tao:1'	3732	09:06:55 22-09-2021
99	saler4	'xoai:1', 'cam:1', 'tao:1'	3672	09:06:57 22-09-2021
100	saler4	'xoai:3', 'cam:10'	3527	21:46:55 25-09-2021
101	saler4	'xoai:3', 'cam:10'	3367	21:47:03 25-09-2021
\.


--
-- Data for Name: historymoney; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.historymoney (nno, username, money_add, date_time) FROM stdin;
699	saler4	1	13:05:16 22-09-2021
700	saler4	1	13:05:19 22-09-2021
701	saler4	1	13:05:21 22-09-2021
702	saler4	1	13:05:25 22-09-2021
703	saler4	1	13:05:27 22-09-2021
704	saler4	900	21:52:47 25-09-2021
\.


--
-- Data for Name: infor; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.infor (username, password, email, ip, id) FROM stdin;
user2	0002	user2@gmail.com	192.168.7.8	1
user7	0007	user7@gmail.com	192.168.7.14	2
user9	009	user9@gmail.com	192.168.1.19	3
use10	1111		1.1.12.3	4
user4	004	\N	192.122.124	5
user1	001	\N	192.123.124	6
user3	003	\N	192.121.124	7
user5	005	\N	192.122.1211	8
user8	008	\N	192.123.1243	10
user11	011	\N	192.121.1244	11
user12	012	\N	192.122.1245	12
user13	013	\N	192.187.1246	13
user14	014	\N	192.123.1247	14
user15	015	\N	192.121.1248	15
user16	016	\N	192.122.1249	16
user17	017	\N	192.187.125	17
user18	018	\N	192.121.1251	18
user19	019	\N	192.122.1252	19
user20	020	\N	192.187.1253	20
user21	021	emnail@gmail.com	1.1.3.4	21
unser22	022	\N	192.123.321	22
user31	031		ada	44
user33	033		ada	45
user36	033		ada	50
user35	035		ada	51
user37	037	037@gmail.com	192.168.037	78
user38	038	038@gmail.com	192.168.038	79
user99	0099	adada	192.168.35.5	80
user100	0099	adada	192.168.35.5	81
user99	0099	adada	192.168.35.5	82
\.


--
-- Data for Name: onfor; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.onfor (ip, realname, phone, id) FROM stdin;
192.168.7.8	dung	0123456785	2
192.168.7.14	hoai	0123456787	7
\.


--
-- Data for Name: salary; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.salary (rank, timework, salary, ids) FROM stdin;
manager	7	300	1
saler37	1	900	44
saler61	1	8446	17
saler40	1	5346	79
saler70	1	4480	19
product_mmger	6	801	2
saler30	1	800	20
saler3	1	550	6
saler52	1	3966	15
saler4	4	4267	4
\.


--
-- Name: history_nno_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.history_nno_seq', 101, true);


--
-- Name: historymoney_nno_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.historymoney_nno_seq', 704, true);


--
-- Name: infor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.infor_id_seq', 82, true);


--
-- Name: fruit fruit_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fruit
    ADD CONSTRAINT fruit_pkey PRIMARY KEY (idf);


--
-- Name: history history_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_pkey PRIMARY KEY (nno);


--
-- Name: historymoney historymoney_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historymoney
    ADD CONSTRAINT historymoney_pkey PRIMARY KEY (nno);


--
-- Name: infor infor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.infor
    ADD CONSTRAINT infor_pkey PRIMARY KEY (id);


--
-- Name: onfor onfor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.onfor
    ADD CONSTRAINT onfor_pkey PRIMARY KEY (ip);


--
-- Name: salary salary_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_pkey PRIMARY KEY (rank);


--
-- Name: onfor onfor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.onfor
    ADD CONSTRAINT onfor_id_fkey FOREIGN KEY (id) REFERENCES public.infor(id) ON DELETE CASCADE;


--
-- Name: salary salary_ids_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_ids_fkey FOREIGN KEY (ids) REFERENCES public.infor(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)

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
-- Name: fruit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.fruit (
    idf integer NOT NULL,
    fruit character varying(60) NOT NULL,
    price integer DEFAULT 10 NOT NULL
);


--
-- Name: history; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.history (
    nno integer NOT NULL,
    username character varying(60) NOT NULL,
    purchase character varying(1000) NOT NULL,
    change character varying(60) NOT NULL,
    date_time character varying(1000) DEFAULT '15:18:08 30-08-2021'::character varying NOT NULL
);


--
-- Name: history_nno_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.history_nno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: history_nno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.history_nno_seq OWNED BY public.history.nno;


--
-- Name: historymoney; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.historymoney (
    nno bigint NOT NULL,
    username character varying(60) NOT NULL,
    money_add character varying(100) NOT NULL,
    date_time character varying(100) NOT NULL
);


--
-- Name: historymoney_nno_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.historymoney_nno_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: historymoney_nno_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.historymoney_nno_seq OWNED BY public.historymoney.nno;


--
-- Name: infor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.infor (
    username character varying(60) NOT NULL,
    password character varying(60) NOT NULL,
    email character varying(60),
    ip character varying(60) NOT NULL,
    id bigint NOT NULL
);


--
-- Name: infor_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.infor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: infor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.infor_id_seq OWNED BY public.infor.id;


--
-- Name: onfor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.onfor (
    ip character varying(60) NOT NULL,
    realname character varying(60) NOT NULL,
    phone character varying(60),
    id integer NOT NULL
);


--
-- Name: salary; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.salary (
    rank character varying(60) NOT NULL,
    timework character varying(60),
    salary integer,
    ids integer DEFAULT 1 NOT NULL
);


--
-- Name: history nno; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.history ALTER COLUMN nno SET DEFAULT nextval('public.history_nno_seq'::regclass);


--
-- Name: historymoney nno; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historymoney ALTER COLUMN nno SET DEFAULT nextval('public.historymoney_nno_seq'::regclass);


--
-- Name: infor id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.infor ALTER COLUMN id SET DEFAULT nextval('public.infor_id_seq'::regclass);


--
-- Data for Name: fruit; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.fruit (idf, fruit, price) FROM stdin;
1	cam	10
2	xoai	20
3	tao	30
4	vai	40
\.


--
-- Data for Name: history; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.history (nno, username, purchase, change, date_time) FROM stdin;
96	saler4	'xoai:1', 'cam:1', 'tao:1'	3852	09:06:50 22-09-2021
97	saler4	'xoai:1', 'cam:1', 'tao:1'	3792	09:06:52 22-09-2021
98	saler4	'xoai:1', 'cam:1', 'tao:1'	3732	09:06:55 22-09-2021
99	saler4	'xoai:1', 'cam:1', 'tao:1'	3672	09:06:57 22-09-2021
100	saler4	'xoai:3', 'cam:10'	3527	21:46:55 25-09-2021
101	saler4	'xoai:3', 'cam:10'	3367	21:47:03 25-09-2021
\.


--
-- Data for Name: historymoney; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.historymoney (nno, username, money_add, date_time) FROM stdin;
699	saler4	1	13:05:16 22-09-2021
700	saler4	1	13:05:19 22-09-2021
701	saler4	1	13:05:21 22-09-2021
702	saler4	1	13:05:25 22-09-2021
703	saler4	1	13:05:27 22-09-2021
704	saler4	900	21:52:47 25-09-2021
\.


--
-- Data for Name: infor; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.infor (username, password, email, ip, id) FROM stdin;
user2	0002	user2@gmail.com	192.168.7.8	1
user7	0007	user7@gmail.com	192.168.7.14	2
user9	009	user9@gmail.com	192.168.1.19	3
use10	1111		1.1.12.3	4
user4	004	\N	192.122.124	5
user1	001	\N	192.123.124	6
user3	003	\N	192.121.124	7
user5	005	\N	192.122.1211	8
user8	008	\N	192.123.1243	10
user11	011	\N	192.121.1244	11
user12	012	\N	192.122.1245	12
user13	013	\N	192.187.1246	13
user14	014	\N	192.123.1247	14
user15	015	\N	192.121.1248	15
user16	016	\N	192.122.1249	16
user17	017	\N	192.187.125	17
user18	018	\N	192.121.1251	18
user19	019	\N	192.122.1252	19
user20	020	\N	192.187.1253	20
user21	021	emnail@gmail.com	1.1.3.4	21
unser22	022	\N	192.123.321	22
user31	031		ada	44
user33	033		ada	45
user36	033		ada	50
user35	035		ada	51
user37	037	037@gmail.com	192.168.037	78
user38	038	038@gmail.com	192.168.038	79
user99	0099	adada	192.168.35.5	80
user100	0099	adada	192.168.35.5	81
user99	0099	adada	192.168.35.5	82
\.


--
-- Data for Name: onfor; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.onfor (ip, realname, phone, id) FROM stdin;
192.168.7.8	dung	0123456785	2
192.168.7.14	hoai	0123456787	7
\.


--
-- Data for Name: salary; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.salary (rank, timework, salary, ids) FROM stdin;
manager	7	300	1
saler37	1	900	44
saler61	1	8446	17
saler40	1	5346	79
saler70	1	4480	19
product_mmger	6	801	2
saler30	1	800	20
saler3	1	550	6
saler52	1	3966	15
saler4	4	4267	4
\.


--
-- Name: history_nno_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.history_nno_seq', 101, true);


--
-- Name: historymoney_nno_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.historymoney_nno_seq', 704, true);


--
-- Name: infor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.infor_id_seq', 82, true);


--
-- Name: fruit fruit_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fruit
    ADD CONSTRAINT fruit_pkey PRIMARY KEY (idf);


--
-- Name: history history_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_pkey PRIMARY KEY (nno);


--
-- Name: historymoney historymoney_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historymoney
    ADD CONSTRAINT historymoney_pkey PRIMARY KEY (nno);


--
-- Name: infor infor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.infor
    ADD CONSTRAINT infor_pkey PRIMARY KEY (id);


--
-- Name: onfor onfor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.onfor
    ADD CONSTRAINT onfor_pkey PRIMARY KEY (ip);


--
-- Name: salary salary_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_pkey PRIMARY KEY (rank);


--
-- Name: onfor onfor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.onfor
    ADD CONSTRAINT onfor_id_fkey FOREIGN KEY (id) REFERENCES public.infor(id) ON DELETE CASCADE;


--
-- Name: salary salary_ids_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_ids_fkey FOREIGN KEY (ids) REFERENCES public.infor(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

