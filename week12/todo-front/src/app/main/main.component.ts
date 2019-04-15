import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { TaskList, Task } from '../shared/models/model';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  public tasksList: TaskList[] = [];
  public tasks: Task[] = [];
  public name: any = '';
  public createdAt: any = '';
  public dueOn: any = '';
  public status: any = '';
  public id: any = '';
  ngOnInit() {
    this.provider.getTasksList().then(res => {
      this.tasksList = res;
      console.log(this.tasksList);
    });
  }
  getTaskFromList(tasklist: TaskList) {
    this.provider.getTasks(tasklist.id).then(res => {
      this.tasks = res;
      console.log(res);
    });
  }

  updateTaskList(tl: TaskList) {
    this.provider.updateTaskList(tl).then(res => {
      console.log(tl.name + ' updated');
    });
  }

  deleteTaskList(tl: TaskList) {
    this.provider.deleteTaskList(tl).then(res => {
      console.log(tl.name + ' deleted');
      this.provider.getTasksList().then(r => {
        this.tasksList = r;
      });
    });
  }
  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.tasksList.push(res);
      });
    }
  }
  // createTask() {
  //   if (this.id !== '') {
  //     this.provider.createTask(t, this.name, this.createdAt, this.dueOn, this.status).
  //     then((task: Task) => {
  //       this.name = '';
  //       this.createdAt = '';
  //       this.dueOn = '';
  //       this.status = '';
  //       this.tasks.push(task.name, rCr, rDue, rSt);
  //     });
  //   }
    // if (this.name !== '') {
    //   this.provider.createTask(this.name).then(resName => {
    //     this.name = '';
    //     this.tasks.push(resName);
    //   });
    // }
    // if (this.createdAt !== '') {
    //   this.provider.createTask(this.createdAt).then(resCr => {
    //     this.createdAt = '';
    //     this.tasks.push(resCr);
    //   });
    // }
    // if (this.dueOn !== '') {
    //   this.provider.createTask(this.dueOn).then(resD => {
    //     this.dueOn = '';
    //     this.tasks.push(resD);
    //   });
    // }
    // if (this.status !== '') {
    //   this.provider.createTask(this.status).then(resStat => {
    //     this.status = '';
    //     this.tasks.push(resStat);
    //   });
    // }
  // }
}
