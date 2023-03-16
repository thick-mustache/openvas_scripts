import sys
import pytz

from datetime import datetime
from icalendar import Calendar, Event
from gvm.connections import UnixSocketConnection
from gvm.errors import GvmError
from gvm.protocols.gmpv224 import Gmp, AliveTest
from gvm.transforms import EtreeCheckCommandTransform

path = '/tmp/gvm/gvmd/gvmd.sock'
connection = UnixSocketConnection(path=path)
transform = EtreeCheckCommandTransform()

nome = 'teste1'
nome_task = 'task_teste'
nome_sch = 'teste_sch'
nome_alert = 'teste_aler'
ports = '33d0cd82-57c6-11e1-8ed1-406186ea4fc5'


try:

    with Gmp(connection=connection, transform=transform) as gmp:
        gmp.authenticate('admin', 'admin')
        
        alive = AliveTest.from_string('CONSIDER_ALIVE')

        gmp.create_target(name=nome, hosts=['192.168.0.1'], port_list_id=ports, alive_test=alive)

        cal = Calendar()
        cal.add('prodid', '-//Foo Bar//')
        cal.add('version', '2.0')

        event = Event()
        event.add('dtstamp', datetime.now(tz=pytz.UTC))
        event.add('dtstart', datetime(2023, 5, 4, tzinfo=pytz.utc))
        cal.add_component(event)
        
        gmp.create_schedule(name=nome_sch, timezone='UTC',  icalendar=cal.to_ical())

        #gmp.create_alert(name=nome_alert,event=)      
        
        #gmp.create_task(name=nome_task, target_id=, alert_ids=, schedule_id=, config_id= , scanner_id=, alterable=1, )

except GvmError as e:
    print('An error occurred', e, file=sys.stderr)
