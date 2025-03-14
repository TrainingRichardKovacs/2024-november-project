alter table circuits add primary key (circuitid);
alter table constructor_results add primary key (constructorresultsid);
alter table constructor_standings add primary key (constructorstandingsid);
alter table constructors add primary key (constructorid);
alter table driver_standings add primary key (driverstandingsid);
alter table drivers add primary key (driverid);
alter table qualifying add primary key (qualifyid);
alter table races add primary key (raceid);
alter table results add primary key (resultid);
alter table sprint_results add primary key (resultid);
alter table status add primary key (statusid);

alter table constructor_standings add constraint fk_const_race foreign key (raceid) references races (raceid);
alter table constructor_standings add constraint fk_const_const foreign key (constructorid) references constructors (constructorid);
alter table constructor_results add constraint fk_cr_race foreign key (raceid) references races (raceid);
alter table constructor_results add constraint fk_cr_cons foreign key (constructorid) references constructors (constructorid);
alter table driver_standings add constraint fk_ds_race foreign key (raceid) references races (raceid);
alter table driver_standings add constraint fk_ds_drive foreign key (driverid) references drivers (driverid);
alter table lap_times add constraint fk_lt_race foreign key (raceid) references races (raceid);
alter table lap_times add constraint fk_lt_drive foreign key (driverid) references drivers (driverid);
alter table pit_stops add constraint fk_ps_race foreign key (raceid) references races (raceid);
alter table pit_stops add constraint fk_ps_drive foreign key (driverid) references drivers (driverid);
alter table qualifying add constraint fk_q_race foreign key (raceid) references races (raceid);
alter table qualifying add constraint fk_q_drive foreign key (driverid) references drivers (driverid);
alter table qualifying add constraint fk_q_const foreign key (constructorid) references constructors (constructorid);
alter table results add constraint fk_r_race foreign key (raceid) references races (raceid);
alter table results add constraint fk_r_drive foreign key (driverid) references drivers (driverid);
alter table results add constraint fk_r_const foreign key (constructorid) references constructors (constructorid);
alter table results add constraint fk_r_status foreign key (statusid) references status (statusid);
alter table sprint_results add constraint fk_sr_race foreign key (raceid) references races (raceid);
alter table sprint_results add constraint fk_sr_drive foreign key (driverid) references drivers (driverid);
alter table sprint_results add constraint fk_sr_const foreign key (constructorid) references constructors (constructorid);
alter table sprint_results add constraint fk_sr_status foreign key (statusid) references status (statusid);